import nmap
import ipaddress
import re

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

print(r"""
  _                    _           
 | |    _             (_)          
 | |    _    _      __ _   _   ___ 
 | |   | |  | |    / _` | | | / _ \
 | |___| |__| |   | (_| | | ||  __/
 |_____|\____/     \__,_| |_| \___|
""")
print("\n****************************************************************")
print("\n* Copyright of Laxmikant Dhawade, 2025                                   *")
print("\n* https://www.linkedin.com/in/laxmikant-dhawade               *")
print("\n****************************************************************")

while True:
    ip_add_entered = input("\nPlease enter the IP address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        if ip_address_obj.is_private:
            print("You entered a private IP address. Consider using a public IP if necessary.")
        print("You entered a valid IP address.")
        break
    except ValueError:
        print("You entered an invalid IP address")

while True:
    print("\nChoose an option:")
    print("1. Scan ports 1 to 1,024")
    print("2. Scan ports 1 to 65,535")
    print("3. Customize port range")
    print("4. Exit")
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        port_min, port_max = 1, 1024
        break
    elif choice == "2":
        port_min, port_max = 1, 65535
        break
    elif choice == "3":
        while True:
            print("Please enter the range of ports you want to scan in format: <int>-<int> (ex: 60-120)")
            port_range = input("Enter port range: ")
            port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
            if port_range_valid:
                port_min = int(port_range_valid.group(1))
                port_max = int(port_range_valid.group(2))
                if 0 <= port_min <= port_max <= 65535:
                    break
                else:
                    print("Invalid port range. Please enter values between 0 and 65535.")
        break
    elif choice == "4":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

nm = nmap.PortScanner()
for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))
        port_status = result['scan'][ip_add_entered]['tcp'][port]['state']
        print(f"Port {port} is {port_status}")
    except Exception as e:
        print(f"Cannot scan port {port}: {e}")
