#prompt user for address
#run traceroute to provided address and back
#display results
#offer to send reults to a printer also

import sys
import ipaddress
import socket
user_input = input("Enter a Fully Qualified Domain Name or IPv4 or IPv6 address\n")
print ("your input was: ", user_input)
#ipaddress.ip_network(user_input)
print(socket.getaddrinfo(user_input, 80, family=0, type=0, proto=0, flags=0))