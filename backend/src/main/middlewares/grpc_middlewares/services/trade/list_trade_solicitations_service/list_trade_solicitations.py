from urllib import response
from src.main.middlewares.grpc_middlewares.protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2_grpc
from src.main.factory.trade.list_trade_solicitations_factory import ListTradeSolicitationsFactory

class ListTradeSolicitationsService(list_trade_solicitations_pb2_grpc.ListTradeSolicitationsServicer):
    def makeListTradeSolicitationsFactory(self, request, context):
        new_request = { 
            "id": request.id,
        }
        result = ListTradeSolicitationsFactory.makeListTradeSolicitationsFactory(new_request)
        print('RESULT', result)
        if (result['statusCode'] == 400):
            response = list_trade_solicitations_pb2.Response(statusCode = result['statusCode'], message = result['body']['message'])
        array_trade = []
        for trade in result['body']:
            user = list_trade_solicitations_pb2.TradeList(
                id = trade['id'],
                received_user_id = trade['received_user_id'],
                sender_user_id = trade['sender_user_id'],
                want_pokemon_id = trade['want_pokemon_id'],
                give_pokemon_id = trade['give_pokemon_id'],
                status = trade['status'],
                want_pokemon_name = trade['want_pokemon_name'],
                want_pokemon_image = trade['want_pokemon_image'],
                give_pokemon_name = trade['give_pokemon_name'],
                give_pokemon_image = trade['give_pokemon_image'],
                received_user_name = trade['received_user_name'],
                sender_user_name = trade['sender_user_name'],
            )
            array_trade.append(user)
        response = list_trade_solicitations_pb2.Response(
            statusCode = result['statusCode'],
            tradeList = array_trade
        )
        print('RESPONSE', response)
        return response
