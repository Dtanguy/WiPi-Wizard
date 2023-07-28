#!/bin/bash

# Exit if any command fails
set -e

# Stop and disable the WiPi-Wizard service
sudo systemctl stop WiPi-Wizard.service
sudo systemctl disable WiPi-Wizard.service

# Remove the WiPi-Wizard service unit file
sudo rm /etc/systemd/system/WiPi-Wizard.service

# Restore the original dnsmasq.conf and hostapd.conf
sudo cp original_dnsmasq.conf /etc/dnsmasq.conf
sudo cp original_hostapd.conf /etc/hostapd/hostapd.conf

# Remove the static IP configuration for the access point
sudo sed -i '/interface wlan0/,/nohook wpa_supplicant/d' /etc/dhcpcd.conf

# Uninstall Flask and other dependencies
sudo pip3 uninstall -y flask

echo "WiPi-Wizard uninstallation completed successfully!"
