import json
from commands import CommandExecutor

class ClientHandler:
    @staticmethod
    def handle_client(client_socket):
        request = client_socket.recv(4096).decode()  # Default utf-8
        try:
            request_data = json.loads(request)
            responses = []

            for req in request_data:  # Iterate through each request in the batch
                command = req.get('method')
                req_id = req.get('id')

                if command:
                    return_code, stdout, stderr = CommandExecutor.execute_command(command)
                    response_data = {
                        'result': return_code,
                        'stdout': stdout,
                        'stderr': stderr,
                        'id': req_id,
                        'error_code': 0
                    }
                else:
                    response_data = {
                        'result': -1,
                        'stdout': '',
                        'stderr': '',
                        'id': req_id,
                        'error_code': 2
                    }
                responses.append(response_data)

        except json.JSONDecodeError:
            responses = [{
                'result': -1,
                'stdout': '',
                'stderr': '',
                'id': None,
                'error_code': 1
            }]

        response = json.dumps(responses)
        client_socket.send(response.encode())
        client_socket.close()
