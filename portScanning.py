import socket
ports=[80,443,3306]
for i in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = sock.connect_ex(('127.0.0.1', i))
    if response == 0:
        print("Port ", i ," is open")
    else:
        print("Port ", i ," is closed")
    sock.close()