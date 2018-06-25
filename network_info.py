#prompt user for address
#run traceroute to provided address and back
#display results
#offer to send reults to a printer also

import netifaces

def localhost_info():
    for i in netifaces.interfaces():
        try:
            # Address
            print("IPv4: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
            print("Subnet Mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
            print("IPv6: ", netifaces.ifaddresses(i)[netifaces.AF_INET6][0]['addr'])
            print("Subnet Mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET6][0]['netmask'])          
            print("\n")
        except:pass
# This is the IP address of the localhost

localhost_info()
