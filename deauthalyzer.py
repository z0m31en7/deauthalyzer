import subprocess
import psutil
import argparse
import signal
import sys
import time
import datetime
import threading
from termcolor import colored

print("\n")
print(colored("         ▄████▀▀█▄", 'green'))
print(colored("       ▄█████████████████▄▄▄", 'green'))
print(colored("     ▄█████.▼.▼.▼.▼.▼.▼▼▼▼", 'green'))
print(" ▒█  ▀▀▄ █▀▀ █▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █░░ █░░█ ▀▀█ █▀▀ █▀▀█ ")
print(" ▒█░▒  █ █▀▀ █▄▄█ █░░█ ░░█░░ █▀▀█ █▄▄█ █░░ █▄▄█ ▄▀░ █▀▀ █▄▄▀ ")
print("  █▄▄▀▀  ▀▀▀ ▀░░▀ ░▀▀▀ ░░▀░░ ▀░░▀ ▀░░▀ ▀▀▀ ▄▄▄█ ▀▀▀ ▀▀▀ ▀░▀▀")
print(colored("     ███████▄.▲.▲.▲.▲▲▲▲▲▲", 'green'))
print(colored("     ██████████████████▀▀▀    (v1)\n", 'green'))
print("                 A tool to monitor and log Wifi-Deauthentication attacks")
print("                                       ~By: Pranjal Goel (z0m31en7) ")


def check_root_privileges():
    if not subprocess.check_output(['id', '-u']).decode().strip() == '0':
        print(colored('\n[x] Need higher privileges, run as root!!!', 'red'))
        sys.exit()

def get_wifi_interfaces():
    interfaces = psutil.net_if_addrs()
    wifi_interfaces = []
    for interface, _ in interfaces.items():
        if interface.startswith('wl'):
           wifi_interfaces.append(interface)

    return wifi_interfaces

def enable_monitor_mode(interface, stealth_mode):
    subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'])
    command = ['sudo', 'airmon-ng', 'start', interface]
    if stealth_mode:
        command.append('1')
    subprocess.run(command)

def extract_mac_address(line):
    mac_index = line.find('SA:') + 4
    mac_address = line[mac_index:mac_index + 17]
    return mac_address

def animate_loading():
    while True:
        for symbol in '|/-\\':
            sys.stdout.write(f'\r{colored("[+] Monitoring deauth packets...", "yellow")} {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)

def detect_deauth_attack(interface, stealth_mode):
    enable_monitor_mode(interface, stealth_mode)
    monitor_interface = f'{interface}mon'
    print(f'{colored("[+] Monitor mode enabled for interface", "green")} {colored(monitor_interface, "cyan")}.')
    command = ['tshark', '-i', monitor_interface, '-Y', 'wlan.fc.type_subtype == 0x0c']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    def signal_handler(sig, frame):
        print('\nExiting...')
        disable_monitor_mode(interface)
        process.terminate()
        sys.exit()

    signal.signal(signal.SIGINT, signal_handler)

    loading_thread = threading.Thread(target=animate_loading)
    loading_thread.daemon = True
    loading_thread.start()

    try:
        for line in process.stdout:
            line = line.decode().strip()
            if line.startswith('Radio tap'):
                loading_thread.join()
                print(f'\n{colored("[!] Deauthentication attack detected!", "red")}')
                print(colored(line, "cyan"))
                mac_address = extract_mac_address(line)
                print(f'{colored("Source MAC address:", "green")} {colored(mac_address, "yellow")}')
                attack_details = [line, f'Source MAC address: {mac_address}']
                write_attack_details(attack_details)
                for _ in range(4):
                    next_line = process.stdout.readline().decode().strip()
                    print(next_line)
                    attack_details.append(next_line)
                    write_attack_details(attack_details)
                break
    except KeyboardInterrupt:
        print('\nExiting...')
    finally:
        disable_monitor_mode(interface)
        process.terminate()

def disable_monitor_mode(interface):
    subprocess.run(['sudo', 'airmon-ng', 'stop', interface])

def write_attack_details(details):
    now = datetime.datetime.now()
    filename = f"deauthlog_{now.strftime('%Y%m%d%H%M%S')}.txt"
    with open(filename, 'a') as file:
        for detail in details:
            file.write(detail + '\n')

parser = argparse.ArgumentParser(description='Detect WiFi deauthentication attacks.')
parser.add_argument('-m', '--mode', dest='stealth', action='store_true', help='Enable stealth mode')
args = parser.parse_args()

# Check root privileges
check_root_privileges()

wifi_interfaces = get_wifi_interfaces()

if not wifi_interfaces:
    print(colored('\n[x] No wireless interfaces found.', 'red'))
    sys.exit()

print(colored('[!] Available WiFi interfaces:', 'green'))
for i, interface in enumerate(wifi_interfaces, 1):
    print(f'{i}. {interface}')

interface_num = input('Enter the number corresponding to the interface to use for monitor mode: ')

try:
    interface_num = int(interface_num)
    if interface_num < 1 or interface_num > len(wifi_interfaces):
        raise ValueError
except ValueError:
    print(colored('Invalid input. Exiting...', 'red'))
    sys.exit()

selected_interface = wifi_interfaces[interface_num - 1]

detect_deauth_attack(selected_interface, args.stealth)
