from urllib import response
from src.main.middlewares.grpc_middlewares.protos.trade.refuse_exchange_proto import refuse_exchange_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.refuse_exchange_proto import refuse_exchange_pb2_grpc
from src.main.factory.trade.refuse_exchange_factory import RefuseExchangeFactory

class RefuseExchangeService(refuse_exchange_pb2_grpc.RefuseExchangeServicer):
    def makeRefuseExchangeFactory(self, request, context):
        new_request = { 
            "id": request.id
        }
        result = RefuseExchangeFactory.makeRefuseExchangeFactory(new_request)
        if (result['statusCode'] == 400):
            response = refuse_exchange_pb2.Response(statusCode = result['statusCode'], message = result['body']['message'])
        response = refuse_exchange_pb2.Response(statusCode = result['statusCode'])
        return response
