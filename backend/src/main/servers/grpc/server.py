from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
import time

import grpc
from src.main.middlewares.grpc_middlewares.protos.user.add_user_account_proto import add_user_account_pb2
from src.main.middlewares.grpc_middlewares.protos.user.add_user_account_proto import add_user_account_pb2_grpc
from src.main.middlewares.grpc_middlewares.services.user.add_user_account_service.add_user_account import AddUserAccountService
#import authenticate
from src.main.middlewares.grpc_middlewares.protos.user.authenticate_user_proto import authenticate_user_pb2
from src.main.middlewares.grpc_middlewares.protos.user.authenticate_user_proto import authenticate_user_pb2_grpc
from src.main.middlewares.grpc_middlewares.services.user.authenticate_user_service.authenticate_user import AuthenticateUserService
#import listUserAccount
from src.main.middlewares.grpc_middlewares.protos.user.list_user_account_proto import list_user_account_pb2
from src.main.middlewares.grpc_middlewares.protos.user.list_user_account_proto import list_user_account_pb2_grpc
from src.main.middlewares.grpc_middlewares.services.user.list_user_account_service.list_user_account import ListUserAccountService
#import listUserInventory
from src.main.middlewares.grpc_middlewares.protos.user.list_user_inventory_proto import list_user_inventory_pb2
from src.main.middlewares.grpc_middlewares.protos.user.list_user_inventory_proto import list_user_inventory_pb2_grpc
from src.main.middlewares.grpc_middlewares.services.user.list_user_inventory_service.list_user_inventory import ListUserInventoryService
#import AddTradeSolicitations
from src.main.middlewares.grpc_middlewares.protos.trade.add_trade_solicitations_proto import add_trade_solicitations_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.add_trade_solicitations_proto import add_trade_solicitations_pb2_grpc
from src.main.middlewares.grpc_middlewares.services.trade.add_trade_solicitations_service.add_trade_solicitations import AddTradeSolicitationsService
#import ListTradeSolicitations
from src.main.middlewares.grpc_middlewares.protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2_grpc
from src.main.middlewares.grpc_middlewares.services.trade.list_trade_solicitations_service.list_trade_solicitations import ListTradeSolicitationsService
#import RefuseExchange
from src.main.middlewares.grpc_middlewares.protos.trade.refuse_exchange_proto import refuse_exchange_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.refuse_exchange_proto import refuse_exchange_pb2_grpc
from src.main.middlewares.grpc_middlewares.services.trade.refuse_exchange_service.refuse_exchange import RefuseExchangeService
#import TradePokemon
from src.main.middlewares.grpc_middlewares.protos.trade.trade_pokemon_proto import trade_pokemon_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.trade_pokemon_proto import trade_pokemon_pb2_grpc
from src.main.middlewares.grpc_middlewares.services.trade.trade_pokemon_service.trade_pokemon import TradePokemonService

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  # add methods
  add_user_account_pb2_grpc.add_AddUserAccountServicer_to_server(AddUserAccountService(), server)
  authenticate_user_pb2_grpc.add_AuthenticateUserServicer_to_server(AuthenticateUserService(), server)
  list_user_account_pb2_grpc.add_ListUserAccountServicer_to_server(ListUserAccountService(), server)
  list_user_inventory_pb2_grpc.add_ListUserInventoryServicer_to_server(ListUserInventoryService(), server)
  add_trade_solicitations_pb2_grpc.add_AddTradeSolicitationsServicer_to_server(AddTradeSolicitationsService(), server)
  list_trade_solicitations_pb2_grpc.add_ListTradeSolicitationsServicer_to_server(ListTradeSolicitationsService(), server)
  refuse_exchange_pb2_grpc.add_RefuseExchangeServicer_to_server(RefuseExchangeService(), server)
  trade_pokemon_pb2_grpc.add_TradePokemonServicer_to_server(TradePokemonService(), server)

  server.add_insecure_port("localhost:50052")
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
  serve()