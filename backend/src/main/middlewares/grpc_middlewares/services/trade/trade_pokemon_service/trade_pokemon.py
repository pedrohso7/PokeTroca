from urllib import response
from src.main.middlewares.grpc_middlewares.protos.trade.trade_pokemon_proto import trade_pokemon_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.trade_pokemon_proto import trade_pokemon_pb2_grpc
from src.main.factory.trade.trade_pokemon_factory import TradePokemonFactory

class TradePokemonService(trade_pokemon_pb2_grpc.TradePokemonServicer):
    def makeTradePokemonFactory(self, request, context):
        new_request = { 
            "id": request.id
        }
        result = TradePokemonFactory.makeTradePokemonFactory(new_request)
        if (result['statusCode'] == 400):
            response = trade_pokemon_pb2.Response(statusCode = result['statusCode'], message = result['body']['message'])
        response = trade_pokemon_pb2.Response(statusCode = result['statusCode'])
        return response
