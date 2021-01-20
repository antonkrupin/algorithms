import socket
from threading import Thread

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12345
separator_token = "<SEP>"

client_sockets = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print('Server Start')
print(f"[*] LIstening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_clients(cs):
    while True:
        try:
            msg = cs.recv(1024).decode('utf-8')
        except ConnectionAbortedError as e:
            print(f"[!] Error: {e}")
            #if cs in client_sockets:
            client_sockets.remove(cs)
            break
        else:
            msg = msg.replace(separator_token, ":")
        
        for client_socket in client_sockets:
            if client_socket == cs:
                continue
            client_socket.send(msg.encode())

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    if client_socket not in client_sockets:
        client_sockets.append(client_socket)
    t = Thread(target=listen_for_clients, args=(client_socket,))
    t.daemon = True
    t.start()

for cs in client_sockets:
    cs.shutdown(socket.SHUT_WR)
    cs.close()
s.close()
