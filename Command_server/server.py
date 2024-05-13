import socket
from client_handler import ClientHandler

class CommandServer:
    def __init__(self, host='0.0.0.0', port=9999):
        self.host = host
        self.port = port

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"[*] Listening on {self.host}:{self.port}")

        while True:
            client, addr = server.accept()
            print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
            ClientHandler.handle_client(client)

if __name__ == '__main__':
    server = CommandServer()
    server.start()
