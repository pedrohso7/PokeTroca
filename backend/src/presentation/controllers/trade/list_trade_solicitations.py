from src.presentation.errors.errors import Errors

class ListTradeSolicitationsController:
  def __init__ (self, listTradeSolicitations):
    self.listTradeSolicitations = listTradeSolicitations

  def list (self, socketRequest):
    requiredFields = ['id']

    for fields in requiredFields:
      if socketRequest[fields] == None:
        return Errors.badRequest(f"Missing {fields} Field")
    trade_list = self.listTradeSolicitations.get(socketRequest["id"])
    return Errors.ok(trade_list)