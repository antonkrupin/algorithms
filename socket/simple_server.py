import socket
import time

host = '127.0.0.1'
port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(4)

print('server start')
connection, address = serverSocket.accept()
while True:
    data = connection.recv(1024)
    print(data.decode('utf-8'))
    if data == 'disconnect':
        serverSocket.close()
    #connection.close()
    #break
    #connection.send(data)