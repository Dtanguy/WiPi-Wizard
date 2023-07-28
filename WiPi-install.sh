#!/bin/bash

# Exit if any command fails
set -e

# Install required packages
sudo apt update
sudo apt install -y hostapd dnsmasq python3-pip

# Install Python dependencies using pip
sudo pip3 install -r requirements.txt

# Create a backup folder and save original configurations
sudo mkdir /etc/WiPi-Wizard-backup
sudo cp /etc/dnsmasq.conf /etc/WiPi-Wizard-backup/original_dnsmasq.conf
sudo cp /etc/hostapd/hostapd.conf /etc/WiPi-Wizard-backup/original_hostapd.conf

# Configure the DHCP server (dnsmasq)
sudo cp dnsmasq.conf /etc/dnsmasq.conf

# Configure the access point (hostapd)
sudo cp hostapd.conf /etc/hostapd/hostapd.conf
sudo sed -i 's/#DAEMON_CONF=""/DAEMON_CONF="\/etc\/hostapd\/hostapd.conf"/' /etc/default/hostapd

# Set static IP for the access point
sudo cat <<EOT >> /etc/dhcpcd.conf

interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant
EOT

# Configure systemd service
sudo cp WiPi-Wizard.service /etc/systemd/system/WiPi-Wizard.service
sudo systemctl enable WiPi-Wizard.service

echo "WiPi-Wizard installation completed successfully!"
echo "Original configurations backed up in /etc/WiPi-Wizard-backup"
echo "Reboot your Raspberry Pi for the changes to take effect."
