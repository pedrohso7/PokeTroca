from src.presentation.controllers.trade.refuse_exchange import RefuseExchangeController
from src.data.usecases.trade.db_refuse_exchange import DbRefuseExchange
from src.infra.database.sqlite.repository.trade.refuse_exchange_repository.refuse_exchange import RefuseExchangeRepo

class RefuseExchangeFactory:
  def makeRefuseExchangeFactory(socketRequest):
    refuseExchangeRepo = RefuseExchangeRepo()
    dbRefuseExchange = DbRefuseExchange(refuseExchangeRepo)
    refuseExchangeController = RefuseExchangeController(dbRefuseExchange)
    result = refuseExchangeController.handle(socketRequest)
    return result