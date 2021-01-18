import socket

host = '127.0.0.1'
port = 12345

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))

while True:
    data = input('Enter data: ')
    if data == 'disconnect':
        clientSocket.close()
        print('You are disconnected from the chat')
        break
    else:
        clientSocket.send(data.encode('utf-8'))
