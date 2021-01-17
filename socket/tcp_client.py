import socket
import threading

HOST = 'localhost'  
PORT = 65432        

server = 'localhost', 65432

def read_sok():
    while True:
        data = s.recv(1024)
        print(data.decode('utf-8'))

name = input('Enter your name: ')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 65432))

s.sendto(('[' + name + '] ' + 'Connect to the server').encode('utf-8'), server)
potok = threading.Thread(target = read_sok)
potok.start()
while True:
    inputText = input()
    s.sendto(('[' + name + '] ' + inputText).encode('utf-8'), server)
