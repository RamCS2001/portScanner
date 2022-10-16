"""portScanning.py: A console application to perform port scanning"""

__author__ = "Ramkumar"
__email__ = "kram.cse.2001@gmail.com"

import ipaddress
import socket
import sys

def portScanning(ip):
    try:
        ports=[80,443,3306,5000]
        for i in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)     
            response = sock.connect_ex((ip, i))
            if response == 10060:
                print("Connection Time-out")
                print("Couldn't connect to "+ ip)
                return
            if response == 0:
                print("Port ", i ," is open")
            sock.close()
    except KeyboardInterrupt:
        print("\n Quiting Scanning !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

print("MENU")
print("1. Scan one IP address")
print("2. Scan Multiple IP addresses")
print("3. Scan a Subnet")
print("4. Enter Host name")
choice= int(input("Enter your choice: "))
if choice==1:
    ip= input("Enter the ip addr to scan: ")
    portScanning(ip)
elif choice==2:
    ips=input("Enter the IP addresses: ")
    ipsList= ips.split(",")
    print(ipsList) 
    for i in ipsList:
        print("Scanning "+ i)
        portScanning(i)

elif choice==3: 
    subnetId= input("Enter the subnet id: ")
    net4 = ipaddress.ip_network(subnetId)
    for ip in net4.hosts:
        print("Scanning "+ ip)
        portScanning(ip)
elif choice==4: 
    hostName= input("Enter the host name ")
    ip = socket.gethostbyname(hostName)
    print(ip)
    portScanning(ip)
