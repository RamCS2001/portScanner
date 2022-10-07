import socket
ports=[80,443,3306,5000]
ip= input("Enter the ip addr to scan: ")
for i in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = sock.connect_ex((ip, i))
    if response == 0:
        print("Port ", i ," is open")
    else:
        print("Port ", i ," is closed")
    sock.close()