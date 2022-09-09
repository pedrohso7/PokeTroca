from urllib import response

from grpc import StatusCode
from src.main.middlewares.grpc_middlewares.protos.user.list_user_account_proto import list_user_account_pb2
from src.main.middlewares.grpc_middlewares.protos.user.list_user_account_proto import list_user_account_pb2_grpc
from src.main.factory.user.list_user_account_factory import ListUserAccountFactory

class ListUserAccountService(list_user_account_pb2_grpc.ListUserAccountServicer):
    def makeListUserAccountFactory(self, request, context):
        print('RESUQEST ID', request.id)
        if (request.id != 0):
            new_request = {
                "id": request.id
            }
        else:
            new_request = {}
        result = ListUserAccountFactory.makeListUserAccountFactory(new_request)
        if (result['statusCode'] == 400):
            response = list_user_account_pb2.Response(statusCode = result['statusCode'], message = result['body']['msg'])
            return response
        array_user = []
        for user in result['body']:
            user = list_user_account_pb2.User(id = user['id'], username = user['username'], name = user['name'])
            array_user.append(user)
        response = list_user_account_pb2.Response(statusCode = result['statusCode'], users = array_user)
        return response