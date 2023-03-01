import subprocess

# Get the name of the network adapter from the user
adapter_name = input("Enter the name of the network adapter you want to use for the VPN connection: ")

# Configure the VPN server adapter
try:
    subprocess.check_call(f"netsh interface set interface '{adapter_name}' admin=enable")
    subprocess.check_call(f"netsh interface ipv4 set address name='{adapter_name}' static 192.168.137.1 255.255.255.0")
    subprocess.check_call("netsh interface ipv4 add route prefix=0.0.0.0/0 interface='{adapter_name}' nexthop=192.168.137.1")
    print("VPN server adapter configuration successful.")
except subprocess.CalledProcessError as e:
    print(f"VPN server adapter configuration failed with error: {e}")

# Enable Internet Connection Sharing (ICS)
try:
    subprocess.check_call("netsh sharing set private allowotherusers enable")
    print("Internet Connection Sharing (ICS) enabled successfully.")
except subprocess.CalledProcessError as e:
    print(f"Enabling Internet Connection Sharing (ICS) failed with error: {e}")

# Configure Windows Firewall for VPN traffic
try:
    subprocess.check_call("netsh advfirewall firewall add rule name='VPN' dir=in action=allow protocol=UDP localport=500,4500")
    print("Windows Firewall configured successfully for VPN traffic.")
except subprocess.CalledProcessError as e:
    print(f"Configuring Windows Firewall for VPN traffic failed with error: {e}")

# Record the configuration in a text file
with open("vpn_config.txt", "w") as f:
    f.write(f"VPN server configuration:\nNetwork adapter: {adapter_name}\nIP address: 192.168.137.1\nSubnet mask: 255.255.255.0\nGateway: 192.168.137.1\nPorts open: UDP 500, UDP 4500")
    print("VPN server configuration saved to vpn_config.txt.")
