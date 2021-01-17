#!/usr/bin/env python3
#!/usr/bin/env python3

import socket
import time

HOST = 'localhost'  
PORT = 65432        

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)

print('Start Server')

while True:
    conn, addr_tosend = s.accept()
    data = conn.recvfrom(1024)
    if addr_tosend not in clients:
        clients.append(addr_tosend)
    print(data[0].decode('utf-8'))
    #with conn:
    while True:
        for client in clients:
            #if client == addr_tosend:
                #continue
            data = conn.recv(1024)
            print('Client send data: ', data.decode('utf-8'))
            conn.sendto(data, client)