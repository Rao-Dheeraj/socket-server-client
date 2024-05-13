import json
import uuid

class RequestSender:
    @staticmethod
    def send_request(commands, connector):
        request_data = []
        for command in commands:
            req_id = str(uuid.uuid4())
            request_data.append({
                'method': command,
                'id': req_id
            })

        connector.send_data(json.dumps(request_data))
        response = connector.receive_data()

        response_data = json.loads(response)
        for resp in response_data:
            print("Result:", resp['result'])
            print("Stdout:", resp['stdout'])
            print("Stderr:", resp['stderr'])
            print("Error code:", resp['error_code'])
            print("ID:", resp['id'])
