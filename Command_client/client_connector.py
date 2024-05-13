import socket

class ClientConnector:
    def __init__(self, host='localhost', port=9999):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client.connect((self.host, self.port))

    def send_data(self, data):
        self.client.send(data.encode())

    def receive_data(self):
        return self.client.recv(4096).decode()

    def close(self):
        self.client.close()
