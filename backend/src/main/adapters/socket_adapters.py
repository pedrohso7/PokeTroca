from src.main.factory.user.add_user_account_factory import AddUserAccountFactory
from src.main.factory.user.authenticate_user_factory import AuthenticateUserFactory
from src.main.factory.user.list_user_account_factory import ListUserAccountFactory
from src.main.factory.user.list_user_inventory_factory import ListUserInventoryFactory
from src.main.factory.trade.list_trade_solicitations_factory import ListTradeSolicitationsFactory
from src.main.factory.trade.add_trade_solicitations_factory import AddTradeSolicitationsFactory
from src.main.factory.trade.trade_pokemon_factory import TradePokemonFactory
from src.main.factory.trade.refuse_exchange_factory import RefuseExchangeFactory
class SocketAdapters:
  def execute(self, socketRequest):
    if (socketRequest["route"] == 'user/create'):
      return AddUserAccountFactory.makeUserAccountFactory(socketRequest["params"])
    if (socketRequest["route"] == 'login'):
      return AuthenticateUserFactory.makeAuthenticateUserFactory(socketRequest["params"])
    if (socketRequest["route"] == 'get-users'):
      return ListUserAccountFactory.makeListUserAccountFactory(socketRequest["params"])
    if (socketRequest["route"] == 'user/inventory'):
      return ListUserInventoryFactory.makeListUserInventoryFactory(socketRequest["params"])
    if (socketRequest["route"] == 'trade/solicitations'):
      return ListTradeSolicitationsFactory.makeListTradeSolicitationsFactory(socketRequest["params"])
    if (socketRequest["route"] == 'trade/create'):
      return AddTradeSolicitationsFactory.makeAddTradeSolicitationsFactory(socketRequest["params"])
    if (socketRequest["route"] == 'trade/accept'):
      return TradePokemonFactory.makeTradePokemonFactory(socketRequest["params"])
    if (socketRequest["route"] == 'trade/refuse'):
      return RefuseExchangeFactory.makeRefuseExchangeFactory(socketRequest["params"])
