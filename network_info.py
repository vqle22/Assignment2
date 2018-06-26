#prompt user for address
#run traceroute to provided address and back
#display results
#offer to send reults to a printer also

import sys
import ipaddress
import socket
import  pexpect


################## use Vinh's code here, get the info about this machine ##########################

################## now get the target from the user ###############################################
user_input = input("Enter a Fully Qualified Domain Name or IPv4 or IPv6 address\n")
print ("your input was: ", user_input)

###############choose between it being an address or an fqdn

#########if it is an ip address, then do this

#######try to create an ip address from the input, catch faulty values
try:
    input_ip_address = ipaddress.ip_network(user_input)
    print("You entered an IPAddress: ", input_ip_address)
    #do we need to be able to tell what kind of address?
    print("ip address version: ", input_ip_address.version)
except ValueError:
    print("input was not a correct IPv4 or IPv6 address")
else:
    target_address = input_ip_address
    print("target address: ", target_address)

#if it is not an ip address, then do this (includes fqdn name errors)
#we need to look at the dns to get info about the fqdn we got as user input
#print("\n", socket.getaddrinfo(user_input, 80, family=0, type=0, proto=0, flags=0))
#socket.getaddrinfo(user_input, 80, family=0, type=0, proto=0, flags=0))

################## now have both addresses, time to run the traceroute ############################

#run the traceroute

#run the ping from here to there using bash commands!
bash_command_string = 'ping -c 10 ' + user_input
#child = pexpect.spawn('ping -c 5 www.google.com')
child = pexpect.spawn(bash_command_string)

#display the specified data from the traceroute, not actually sure what that data is yet
while 1:
    line = child.readline()
    if not line: break
    print(line)


################## traceroute ran, output displayed, not prompt to send to a printer ##############




