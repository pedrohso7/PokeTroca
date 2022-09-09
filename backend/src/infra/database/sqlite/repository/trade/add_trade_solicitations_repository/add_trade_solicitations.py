from src.data.protocols.trade.add_trade_solicitations_repository import AddTradeSolicitationsRepository as AddTradeSolicitationsRepositoryInterface
from src.infra.database.sqlite.views.trade.trade_view import *

class AddTradeSolicitationsRepo(AddTradeSolicitationsRepositoryInterface):
  
  def add (self, tradeSolicitationData):
    insertTrade(tradeSolicitationData)