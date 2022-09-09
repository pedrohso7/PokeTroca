from src.domain.usecases.trade.refuse_exchange import RefuseExchange as RefuseExchangeInterface

class DbRefuseExchange(RefuseExchangeInterface):
  
  def __init__(self, refuse_exchange_repository):
    self.refuse_exchange_repository = refuse_exchange_repository

  def update (self, id):
    return self.refuse_exchange_repository.update(id)