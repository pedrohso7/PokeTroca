from src.presentation.controllers.trade.list_trade_solicitations import ListTradeSolicitationsController
from src.data.usecases.trade.db_list_trade_solicitations import DbListTradeSolicitations
from src.infra.database.sqlite.repository.trade.list_trade_solicitations_repository.list_trade_solicitations import ListTradeSolicitationsRepo

class ListTradeSolicitationsFactory:
  def makeListTradeSolicitationsFactory(socketRequest):
    listTradeSolicitationsRepo = ListTradeSolicitationsRepo()
    dbListTradeSolicitations = DbListTradeSolicitations(listTradeSolicitationsRepo)
    listTradeSolicitationController = ListTradeSolicitationsController(dbListTradeSolicitations)
    result = listTradeSolicitationController.list(socketRequest)
    return result