from urllib import response
from src.main.middlewares.grpc_middlewares.protos.user.authenticate_user_proto import authenticate_user_pb2
from src.main.middlewares.grpc_middlewares.protos.user.authenticate_user_proto import authenticate_user_pb2_grpc
from src.main.factory.user.authenticate_user_factory import AuthenticateUserFactory

class AuthenticateUserService(authenticate_user_pb2_grpc.AuthenticateUserServicer):
    def makeAuthenticateUserFactory(self, request, context):
        new_request = { 
            "username": request.username,
            "password": request.password,
        }
        result = AuthenticateUserFactory.makeAuthenticateUserFactory(new_request)
        response = authenticate_user_pb2.Response()
        response.statusCode = result['statusCode']
        if (result['statusCode'] == 400):
            response.message = result['body']['msg']
            return response
        response.id = result['body']['id']
        response.username = result['body']['username']
        response.name = result['body']['name']
        return response
