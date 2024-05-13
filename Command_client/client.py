from client_connector import ClientConnector
from request_sender import RequestSender

def main():
    connector = ClientConnector()
    connector.connect()

    num_requests = int(input("Enter the number of commands to execute: "))
    commands = [input(f"Enter command {i+1}: ") for i in range(num_requests)]

    RequestSender.send_request(commands, connector)

    connector.close()

if __name__ == '__main__':
    main()
