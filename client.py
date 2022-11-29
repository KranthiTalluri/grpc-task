import grpc
import unitask_pb2_grpc as pb2_grpc
import unitask_pb2 as pb2
from flask import Flask, render_template, request, jsonify
import json


class UnitaskClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'server'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnitaskStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get_grpc_response', methods=['GET', 'POST'])
def get_grpc_server_resp():
    try:
        print('H0')
        print(json.loads(request.data)['text_input'])
        client_data = json.loads(request.data)['text_input']

        print('H1')

        client = UnitaskClient()
        print('H2')
        result = client.get_url(message=client_data)

        # print(f'{result}')

        # print('Message', result)

        print('H3')

        response = jsonify({
            'server_response': result.message
        })

        print('H4')

        response.headers.add('Access-Control-Allow-Origin', '*')

        print('H5')

        return response
    except:
        response = jsonify({
            'server_response': "NuLL",
            'server_error': 'Internal serval error'
        })

        response.headers.add('Access-Control-Allow-Origin', '*')

        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)