import grpc
from concurrent import futures
import time
from datetime import datetime
import unitask_pb2_grpc as pb2_grpc
import unitask_pb2 as pb2
import os

log_file_dir = 'logs'
log_file_name = 'server.txt'


class UnitaskService(pb2_grpc.UnitaskServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        print('Server', request)
        message = request.message
        write_log(log_file_dir, log_file_name, message)
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)

def write_log(_log_dir, _log_file_name, client_message):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    try:
        with open(_log_dir + '/' + _log_file_name, 'a') as f:
            f.write(timestampStr + ';' + client_message)
            f.write('\n')
    except Exception as err:
        print("Error", err)


def create_log_dir(_log_dir, _log_file_name):
    if not os.path.exists(_log_dir):
        os.makedirs(_log_dir)
    
    # If log already exists then don't write the headers
    if not os.path.exists(_log_dir + '/' + _log_file_name):
        with open(_log_dir + '/' + _log_file_name, 'w') as f:
            f.truncate(0)
            f.write("timestamp;client_message;") # Headers
            f.write('\n')



def serve():
    create_log_dir(log_file_dir, log_file_name)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnitaskServicer_to_server(UnitaskService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()