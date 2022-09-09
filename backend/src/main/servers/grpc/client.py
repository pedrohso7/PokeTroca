from src.main.middlewares.grpc_middlewares.protos.user.add_user_account_proto import add_user_account_pb2
from src.main.middlewares.grpc_middlewares.protos.user.add_user_account_proto import add_user_account_pb2_grpc
#Authenticate
from src.main.middlewares.grpc_middlewares.protos.user.authenticate_user_proto import authenticate_user_pb2
from src.main.middlewares.grpc_middlewares.protos.user.authenticate_user_proto import authenticate_user_pb2_grpc
#ListUserAccount
from src.main.middlewares.grpc_middlewares.protos.user.list_user_account_proto import list_user_account_pb2
from src.main.middlewares.grpc_middlewares.protos.user.list_user_account_proto import list_user_account_pb2_grpc
#ListUserInventory
from src.main.middlewares.grpc_middlewares.protos.user.list_user_inventory_proto import list_user_inventory_pb2
from src.main.middlewares.grpc_middlewares.protos.user.list_user_inventory_proto import list_user_inventory_pb2_grpc
#AddTradeSolicitations
from src.main.middlewares.grpc_middlewares.protos.trade.add_trade_solicitations_proto import add_trade_solicitations_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.add_trade_solicitations_proto import add_trade_solicitations_pb2_grpc
#ListTradeSolicitations
from src.main.middlewares.grpc_middlewares.protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2_grpc
#RefuseExchange
from src.main.middlewares.grpc_middlewares.protos.trade.refuse_exchange_proto import refuse_exchange_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.refuse_exchange_proto import refuse_exchange_pb2_grpc
#TradePokemon
from src.main.middlewares.grpc_middlewares.protos.trade.trade_pokemon_proto import trade_pokemon_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.trade_pokemon_proto import trade_pokemon_pb2_grpc
import grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        route = 'trade/solicitations'
        if (route == 'login'):
            stub = authenticate_user_pb2_grpc.AuthenticateUserStub(channel)
            request = authenticate_user_pb2.Request(username = "teste82@teste.com", password = "teste123")
            response = stub.makeAuthenticateUserFactory(request)
            print('RESPONSE', response)
            return response
        if (route == 'user/create'):
            stub = add_user_account_pb2_grpc.AddUserAccountStub(channel)
            request = add_user_account_pb2.Request(username = "teste81@teste.com", password = "teste123", name = "Pedro Oliveira")
            response = stub.makeUserAccountFactory(request)
            print('RESPONSE', response)
            return response
        if (route == 'get-user'):
            stub = list_user_account_pb2_grpc.ListUserAccountStub(channel)
            request = list_user_account_pb2.Request()
            response = stub.makeListUserAccountFactory(request)
            print('RESPONSE', response)
            return response
        if (route == 'user/inventory'):
            stub = list_user_inventory_pb2_grpc.ListUserInventoryStub(channel)
            request = list_user_inventory_pb2.Request(id = 4)
            response = stub.makeListUserInventoryFactory(request)
            print('RESPONSE', response)
            return response
        if (route == 'trade/create'):
            stub = add_trade_solicitations_pb2_grpc.AddTradeSolicitationsStub(channel)
            request = add_trade_solicitations_pb2.Request(
                received_user_id = 1,
                sender_user_id = 2,
                want_pokemon_id = 2,
                give_pokemon_id = 3,
            )
            response = stub.makeAddTradeSolicitationsFactory(request)
            print('RESPONSE', response)
            return response
        if (route == 'trade/solicitations'):
            stub = list_trade_solicitations_pb2_grpc.ListTradeSolicitationsStub(channel)
            request = list_trade_solicitations_pb2.Request(id = 4)
            response = stub.makeListTradeSolicitationsFactory(request)
            print('RESPONSE', response)
            return response
        if (route == 'trade/refuse'):
            stub = refuse_exchange_pb2_grpc.RefuseExchangeStub(channel)
            request = refuse_exchange_pb2.Request(id = 1)
            response = stub.makeRefuseExchangeFactory(request)
            print('RESPONSE', response)
            return response
        if (route == 'trade/accecpt'):
            stub = trade_pokemon_pb2_grpc.TradePokemonStub(channel)
            request = trade_pokemon_pb2.Request(id = 1)
            response = stub.makeTradePokemonFactory(request)
            print('RESPONSE', response)
            return response

if __name__ == "__main__":
    run()