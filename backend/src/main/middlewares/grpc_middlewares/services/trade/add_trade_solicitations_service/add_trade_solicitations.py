from urllib import response
from src.main.middlewares.grpc_middlewares.protos.trade.add_trade_solicitations_proto import add_trade_solicitations_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.add_trade_solicitations_proto import add_trade_solicitations_pb2_grpc
from src.main.factory.trade.add_trade_solicitations_factory import AddTradeSolicitationsFactory

class AddTradeSolicitationsService(add_trade_solicitations_pb2_grpc.AddTradeSolicitationsServicer):
    def makeAddTradeSolicitationsFactory(self, request, context):
        new_request = { 
            "received_user_id": request.received_user_id,
            "sender_user_id": request.sender_user_id,
            "want_pokemon_id": request.want_pokemon_id,
            "give_pokemon_id": request.give_pokemon_id,
        }
        result = AddTradeSolicitationsFactory.makeAddTradeSolicitationsFactory(new_request)
        if (result['statusCode'] == 400):
            response = add_trade_solicitations_pb2.Response(statusCode = result['statusCode'], message = result['body']['message'])
        response = add_trade_solicitations_pb2.Response(statusCode = result['statusCode'])
        return response
