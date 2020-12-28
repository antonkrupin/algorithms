from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 12345))

while True:
    string = input('Enter the message (type "end" for disconnect): ')
    if string != 'end':
        string_encode = string.encode('utf-8')
        s.send(string_encode)
        print(s.recv(1024).strip())
    else:
        break