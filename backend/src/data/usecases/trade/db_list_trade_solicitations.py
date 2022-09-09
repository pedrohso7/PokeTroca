from src.domain.usecases.trade.list_trade_solicitations import ListTradeSolicitations as ListTradeSolicitationsInterface

class DbListTradeSolicitations(ListTradeSolicitationsInterface):
  
  def __init__(self, list_trade_solicitations_repository):
    self.list_trade_solicitations_repository = list_trade_solicitations_repository

  def get (self, id):
    return self.list_trade_solicitations_repository.get(id)