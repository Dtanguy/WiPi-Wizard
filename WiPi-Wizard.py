#!/usr/bin/env python3

import subprocess
import time
from flask import Flask, request, render_template

app = Flask(__name__)

HOTSPOT_SSID = "MyHotspot"  # Change this to the SSID of your hotspot
WIFI_CONFIG_FILE = "/etc/wpa_supplicant/wpa_supplicant.conf"

def check_wifi():
    try:
        subprocess.check_output(["nmcli", "d", "wifi"])
        return True
    except subprocess.CalledProcessError:
        return False

def get_nearby_wifi():
    try:
        wifi_list = subprocess.check_output(["nmcli", "d", "wifi", "list"]).decode("utf-8")
        return [line.split()[0] for line in wifi_list.splitlines()[1:]]
    except subprocess.CalledProcessError:
        return []

def create_hotspot():
    subprocess.run(["sudo", "systemctl", "stop", "hostapd"])
    subprocess.run(["sudo", "systemctl", "stop", "dnsmasq"])
    subprocess.run(["sudo", "nmcli", "radio", "wifi", "off"])
    subprocess.run(["sudo", "rfkill", "unblock", "wlan"])
    subprocess.run(["sudo", "ifconfig", "wlan0", "192.168.4.1", "netmask", "255.255.255.0"])
    subprocess.run(["sudo", "hostapd", "/etc/hostapd/hostapd.conf"])
    subprocess.run(["sudo", "systemctl", "start", "dnsmasq"])

def configure_wifi(ssid, passphrase):
    with open(WIFI_CONFIG_FILE, "w") as f:
        f.write(f"ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n")
        f.write(f"update_config=1\n")
        f.write(f"country=US\n\n")  # Replace 'US' with your country code
        f.write(f"network={{\n    ssid=\"{ssid}\"\n    psk=\"{passphrase}\"\n}}\n")


@app.route('/')
def index():
    nearby_wifi = get_nearby_wifi()
    return render_template('index.html', wifi_list=nearby_wifi)

@app.route('/configure', methods=['POST'])
def configure():
    ssid = request.form['ssid']
    passphrase = request.form['passphrase']
    if ssid and passphrase:
        configure_wifi(ssid, passphrase)
        return "<h1>Wi-Fi Configuration Successful!</h1>"
    else:
        return "<h1>Bad Request</h1>"

def main():
    while True:
        if not check_wifi():
            create_hotspot()
            app.run(host='0.0.0.0', port=80)
        time.sleep(10)

if __name__ == "__main__":
    main()