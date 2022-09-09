from protos.user.add_user_account_proto import add_user_account_pb2
from protos.user.add_user_account_proto import add_user_account_pb2_grpc
#Authenticate
from protos.user.authenticate_user_proto import authenticate_user_pb2
from protos.user.authenticate_user_proto import authenticate_user_pb2_grpc
#ListUserAccount
from protos.user.list_user_account_proto import list_user_account_pb2
from protos.user.list_user_account_proto import list_user_account_pb2_grpc
#ListUserInventory
from protos.user.list_user_inventory_proto import list_user_inventory_pb2
from protos.user.list_user_inventory_proto import list_user_inventory_pb2_grpc
#AddTradeSolicitations
from protos.trade.add_trade_solicitations_proto import add_trade_solicitations_pb2
from protos.trade.add_trade_solicitations_proto import add_trade_solicitations_pb2_grpc
#ListTradeSolicitations
from protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2
from protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2_grpc
#RefuseExchange
from protos.trade.refuse_exchange_proto import refuse_exchange_pb2
from protos.trade.refuse_exchange_proto import refuse_exchange_pb2_grpc
#TradePokemon
from protos.trade.trade_pokemon_proto import trade_pokemon_pb2
from protos.trade.trade_pokemon_proto import trade_pokemon_pb2_grpc

import grpc

def runGRPCMethod(route, params):
    with grpc.insecure_channel('localhost:50052') as channel:
        if (route == 'login'):
            stub = authenticate_user_pb2_grpc.AuthenticateUserStub(channel)
            request = authenticate_user_pb2.Request(username = params['username'], password = params['password'])
            response = stub.makeAuthenticateUserFactory(request)
            return response
        if (route == 'user/create'):
            stub = add_user_account_pb2_grpc.AddUserAccountStub(channel)
            request = add_user_account_pb2.Request(username = params['username'], password = params['password'], name = params['name'])
            response = stub.makeUserAccountFactory(request)
            return response
        if (route == 'get-users'):
            stub = list_user_account_pb2_grpc.ListUserAccountStub(channel)
            request = list_user_account_pb2.Request(id = params['id'])
            response = stub.makeListUserAccountFactory(request)
            return response
        if (route == 'user/inventory'):
            stub = list_user_inventory_pb2_grpc.ListUserInventoryStub(channel)
            request = list_user_inventory_pb2.Request(id = params['id'])
            response = stub.makeListUserInventoryFactory(request)
            return response
        if (route == 'trade/create'):
            stub = add_trade_solicitations_pb2_grpc.AddTradeSolicitationsStub(channel)
            request = add_trade_solicitations_pb2.Request(
                received_user_id = params['received_user_id'],
                sender_user_id = params['sender_user_id'],
                want_pokemon_id = params['want_pokemon_id'],
                give_pokemon_id = params['give_pokemon_id'],
            )
            response = stub.makeAddTradeSolicitationsFactory(request)
            return response
        if (route == 'trade/solicitations'):
            stub = list_trade_solicitations_pb2_grpc.ListTradeSolicitationsStub(channel)
            request = list_trade_solicitations_pb2.Request(id = params['id'])
            response = stub.makeListTradeSolicitationsFactory(request)
            return response
        if (route == 'trade/refuse'):
            stub = refuse_exchange_pb2_grpc.RefuseExchangeStub(channel)
            request = refuse_exchange_pb2.Request(id = params['id'])
            response = stub.makeRefuseExchangeFactory(request)
            return response
        if (route == 'trade/accept'):
            stub = trade_pokemon_pb2_grpc.TradePokemonStub(channel)
            request = trade_pokemon_pb2.Request(id = params['id'])
            response = stub.makeTradePokemonFactory(request)
            return response