from src.data.protocols.trade.refuse_exchange_repository import RefuseExchangeRepository as RefuseExchangeRepositoryInterface
from src.infra.database.sqlite.views.trade.trade_view import *

class RefuseExchangeRepo(RefuseExchangeRepositoryInterface):
  
  def update (self, id):
    updateTradeStatus(id)