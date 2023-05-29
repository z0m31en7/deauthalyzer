#!/bin/bash

# Function to check if a command is available
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if ! command_exists python3; then
  read -p "Python is not installed. Do you want to install it? (y/n): " install_python
  if [ "$install_python" = "y" ]; then
    sudo apt-get update
    sudo apt-get install -y python3
  else
    echo "Python installation skipped. Exiting..."
    exit 1
  fi
fi

# Check if pip is installed
if ! command_exists pip3; then
  read -p "pip is not installed. Do you want to install it? (y/n): " install_pip
  if [ "$install_pip" = "y" ]; then
    sudo apt-get update
    sudo apt-get install -y python3-pip
  else
    echo "pip installation skipped. Exiting..."
    exit 1
  fi
fi

# Install required system packages
sudo apt-get update
sudo apt-get install -y tshark aircrack-ng

# Install required Python packages
pip3 install psutil signal termcolor

echo "Installation complete."

