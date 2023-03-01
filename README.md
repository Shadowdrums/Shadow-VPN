# Shadow-VPN
make a computer a VPN server with python

This script configures a Windows computer to act as a VPN server. It performs the following steps:

Asks the user to input the name of the network adapter to use for the VPN connection.
Configures the specified network adapter to use a static IP address of 192.168.137.1 with a subnet mask of 255.255.255.0.
Adds a default route through the specified network adapter.
Enables Internet Connection Sharing (ICS) to allow other devices to access the Internet through the VPN server.
Configures Windows Firewall to allow VPN traffic through UDP ports 500 and 4500.
Records the VPN server configuration in a text file named vpn_config.txt.
The subprocess module is used to execute Windows command-line commands. The check_call() function is used to execute the commands and raise a CalledProcessError if the command returns a non-zero exit code. The with statement is used to open a file and automatically close it when the block is exited.

Overall, this script automates the process of configuring a Windows computer to act as a VPN server, which can be useful for remote access or securing network traffic.
