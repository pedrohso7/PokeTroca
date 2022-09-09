from src.presentation.controllers.trade.add_trade_solicitations import AddTradeSolicitationsController
from src.data.usecases.trade.db_add_trade_solicitations import DbAddTradeSolicitations
from src.infra.database.sqlite.repository.trade.add_trade_solicitations_repository.add_trade_solicitations import AddTradeSolicitationsRepo

class AddTradeSolicitationsFactory:
  def makeAddTradeSolicitationsFactory(socketRequest):
    addTradeSolicitationsRepo = AddTradeSolicitationsRepo()
    dbaddTradeSolicitations = DbAddTradeSolicitations(addTradeSolicitationsRepo)
    addTradeSolicitationController = AddTradeSolicitationsController(dbaddTradeSolicitations)
    result = addTradeSolicitationController.handle(socketRequest)
    return result