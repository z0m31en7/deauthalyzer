<h1 align="center" id="title">Deauthalyzer</h1><br>

<p align="center"><img src="https://socialify.git.ci/z0m31en7/deauthalyzer/image?font=Source%20Code%20Pro&amp;logo=https%3A%2F%2Fraw.githubusercontent.com%2Fz0m31en7%2Fdeauthalyzer%2Fmain%2Flogo.png&amp;name=1&amp;owner=1&amp;pattern=Floating%20Cogs&amp;theme=Dark" alt="project-image"></p><br>

<p id="description">Deauthalyzer is a script designed to monitor WiFi networks and detect de-authentication attacks. It utilizes packet sniffing and analysis techniques to identify de-authentication attack packets and provide relevant information about the attack. <br><br>This tool can be used by individuals or organizations that are interested in monitoring and protecting their WiFi networks from deauthentication attacks. This tool is particularly useful for:</p><br>

* Network Administrators: Network administrators can use this tool to monitor their WiFi networks for any potential deauthentication attacks. It helps them identify and analyze the attacks, allowing them to take appropriate security measures to protect their network.

* Security Researchers: Security researchers can utilize this tool to study and analyze deauthentication attacks in order to understand their techniques, patterns, and potential vulnerabilities in WiFi networks. This can contribute to the development of stronger security protocols and countermeasures.

* Penetration Testers: Penetration testers can employ this tool as part of their assessment to evaluate the security posture of a WiFi network. By simulating deauthentication attacks, they can assess the network's resilience and identify any weaknesses that could be exploited.

* WiFi Network Owners: Individuals or organizations that operate WiFi networks, such as cafes, businesses, or public places, can utilize this tool to actively monitor their network for deauthentication attacks. It enables them to detect and respond to any malicious activities that could disrupt the network's availability.

* Security Enthusiasts: Security enthusiasts and hobbyists interested in WiFi security can explore and experiment with this tool to gain a better understanding of deauthentication attacks and the techniques used to detect and mitigate them.

<br><p align="center"><img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&amp;logo=linux&amp;logoColor=black" alt="shields"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&amp;logo=windows&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/PyCharm-000000.svg?style=for-the-badge&amp;logo=PyCharm&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&amp;logo=kali-linux&amp;logoColor=white" alt="shields"></p><br>


<p align="center"><img src="https://raw.githubusercontent.com/z0m31en7/deauthalyzer/main/logo.png" alt="project-logo"></p>


<br><h2>💡 Features:</h2>

*   Monitors WiFi networks for de-authentication attack packets.
*   Displays information about the detected attack including the source MAC address.
*   Provides the option to enable stealth mode during monitoring.
*   Records details of detected attacks in a log file.
<br><h2>📺 Preview:</h2><br>

<p align="center"><img src="https://raw.githubusercontent.com/z0m31en7/deauthalyzer/main/deauthalyzer.png" alt="project-logo"></p><br>

  
 

<h2>🛠️ Installation Steps:</h2><br>

```
git clone https://github.com/z0m31en7/deauthalyzer.git
```

```
cd deauthalyzer && sudo ./install.sh
```

```
sudo python deauthalyzer.py
```

<br><h2>🎛 Usage:</h2>

1\. Run the script with root privileges. <br><br>2. The script will display a list of available WiFi interfaces. Select the number corresponding to the interface you want to use for monitor mode. <br><br>3. The script will start monitoring the selected WiFi interface for de-authentication attack packets. If an attack is detected it will display information about the attack including the source MAC address. <br><br>4. The script will also record the details of detected attacks in a text file. Each attack will be stored in a separate file with the name deauthlog\_dateandtime.txt where dateandtime represents the timestamp when the attack was detected.<br>

  
  
<br><h2>🪛 Troubleshooting:</h2>
*  If you encounter any issues with the script, ensure that you have the necessary dependencies and tools installed correctly.

*   Make sure you run the script with root privileges or use sudo.
*   If the script fails to detect any wireless interfaces, ensure that your system has WiFi capabilities and the interfaces are properly recognized.
*   If you experience any problems related to the packet capturing process, make sure airmon-ng and tshark are installed correctly and accessible from the command line.
* If the issue still persists you can report the issue you are facing.

<br><h2>🛡️ License:</h2><br>
This project is licensed under the <a href="https://github.com/z0m31en7/deauthalyzer/blob/main/LICENSE">MIT-LICENSE</a>