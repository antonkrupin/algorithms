from socketserver import BaseRequestHandler, TCPServer

class TestTCPHandler(BaseRequestHandler):

    def handle(self):
        print('Handle activated', self.client_address)
        while True:
            self.data = self.request.recv(1024).strip()
            print(f'server recieved - {self.data}')
            self.request.send(self.data + b' (answer from server)')

server = TCPServer(('localhost', 12345), TestTCPHandler)
server.serve_forever()