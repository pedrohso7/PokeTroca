from src.domain.usecases.trade.add_trade_solicitations import AddTradeSolicitations as AddTradeSolicitationsInterface

class DbAddTradeSolicitations(AddTradeSolicitationsInterface):
  
  def __init__(self, add_trade_solicitations_repository):
    self.add_trade_solicitations_repository = add_trade_solicitations_repository

  def add (self, tradeSolicitationData):
    return self.add_trade_solicitations_repository.add(tradeSolicitationData)