import socket

from threading import Thread

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345
separator_token = "<SEP>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((SERVER_HOST, SERVER_PORT))

name = input("Enter your name: ")
print('Type "disconnect" for disconnect from the server')

def listen_for_messages():
    while True:
        message = s.recv(1024).decode('utf-8')
        print(message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

s.send(('[' + name + '] ' + 'connected to the chat').encode('utf-8'))

while True:
    to_send = input()
    if to_send.lower() == 'disconnect':
        s.send(('[' + name+ '] ' + 'disconnected from the chat').encode('utf-8'))
        s.shutdown(socket.SHUT_WR)
        s.close()
        break
    s.send(('[' + name + ']: ' + to_send).encode('utf-8'))

s.close()