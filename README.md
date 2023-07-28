# WiPi-Wizard

WiPi-Wizard is a Raspberry Pi project that allows you to set up a Wi-Fi hotspot when no known Wi-Fi networks are available. The hotspot allows users to connect to a web page where they can select a new Wi-Fi network and provide the passphrase for connection.

## Features

- Automatically creates a Wi-Fi hotspot when no known networks are available.
- Provides a web page for users to select and connect to a new Wi-Fi network.
- Easy installation and setup with an installation script.

## Requirements

- Raspberry Pi with Wi-Fi support (Make sure your Wi-Fi adapter supports Access Point mode).
- Raspberry Pi OS or a Debian-based operating system.

## Installation

1. Clone this repository:

- git clone https://github.com/dtanguy/WiPi-Wizard.git
- cd WiPi-Wizard

2. Run the installation script:

- chmod +x WiPi-install.sh
- ./WiPi-install.sh


3. Reboot your Raspberry Pi for the changes to take effect.

## Usage

Once the installation is complete and your Raspberry Pi starts up, it will automatically create a Wi-Fi hotspot if no known Wi-Fi networks are available. Connect your device to the hotspot and open a web browser. The WiPi-Wizard page will automatically load, allowing you to select a new Wi-Fi network and provide the passphrase for connection.

## Uninstallation

To uninstall WiPi-Wizard and revert the changes:

1. Run the uninstallation script:

- chmod +x WiPi-uninstall.sh
- ./WiPi-uninstall.sh

2. Reboot your Raspberry Pi.

## Configuration

- You can customize the hotspot SSID and other settings by modifying the `hostapd.conf` file before running the installation script.

## Troubleshooting

- If you encounter any issues, please refer to the [Troubleshooting](TROUBLESHOOTING.md) guide for common solutions.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
