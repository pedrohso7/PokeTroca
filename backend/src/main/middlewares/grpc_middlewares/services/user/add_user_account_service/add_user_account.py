from urllib import response
from src.main.middlewares.grpc_middlewares.protos.user.add_user_account_proto import add_user_account_pb2
from src.main.middlewares.grpc_middlewares.protos.user.add_user_account_proto import add_user_account_pb2_grpc
from src.main.factory.user.add_user_account_factory import AddUserAccountFactory

class AddUserAccountService(add_user_account_pb2_grpc.AddUserAccountServicer):
    def makeUserAccountFactory(self, request, context):
        new_request = { 
            "username": request.username,
            "password": request.password,
            "name": request.name,
        }
        result = AddUserAccountFactory.makeUserAccountFactory(new_request)
        response = add_user_account_pb2.Response()
        response.statusCode = result['statusCode']
        return response
