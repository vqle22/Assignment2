#prompt user for address
#run traceroute to provided address and back
#display results
#offer to send reults to a printer also

import sys
import ipaddress
import socket
import pexpect
import netifaces


################## use Vinh's code here, get the info about this machine ##########################
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

################## now get the target from the user #################################
################## choose between it being an address or an fqdn ###############
user_input = ""
while user_input != "FQDN" and user_input != "IPA":
    user_input = input("Enter FQDN or IPA: ")
    if user_input != "FQDN" and user_input != "IPA":
        print("You must type FQDN or IPA!")

#########if it is an ip address, then do this
#######try to create an ip address from the input, catch faulty values #######
if user_input == "IPA":
    ipa_input = input("Enter a Fully Qualified Domain Name or IPv4 or IPv6 address: \n")
    print ("your input was: ", ipa_input)
    try:
        input_ip_address = ipaddress.ip_network(ipa_input)
        print("You entered an IPAddress: ", input_ip_address)
        #do we need to be able to tell what kind of address?
        print("ip address version: ", input_ip_address.version)
    except ValueError:
        print("input was not a correct IPv4 or IPv6 address")
    else:
        target_address = input_ip_address
        print("target address: ", target_address)

#if it is not an ip address, then do this (includes fqdn name errors)

# if user_input = "FQDN":

#we need to look at the dns to get info about the fqdn we got as user input
#print("\n", socket.getaddrinfo(user_input, 80, family=0, type=0, proto=0, flags=0))
#socket.getaddrinfo(user_input, 80, family=0, type=0, proto=0, flags=0))

################## now have both addresses, time to run the traceroute ############################

#run the traceroute

#run the ping from here to there using bash commands!
bash_command_string = 'ping -c 10 ' + ipa_input
#child = pexpect.spawn('ping -c 5 www.google.com')
child = pexpect.spawn(bash_command_string)

#display the specified data from the traceroute, not actually sure what that data is yet
while 1:
    line = child.readline()
    if not line: break
    print(line)


################## traceroute ran, output displayed, not prompt to send to a printer ##############
