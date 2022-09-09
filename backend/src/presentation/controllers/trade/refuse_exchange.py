from src.presentation.errors.errors import Errors

class RefuseExchangeController:
  def __init__ (self, refuseExchange):
    self.refuseExchange = refuseExchange

  def handle (self, socketRequest):
    requiredFields = ['id']

    for fields in requiredFields:
      if socketRequest[fields] == None:
        return Errors.badRequest(f"Missing {fields} Field")
    self.refuseExchange.update(socketRequest["id"])
    return Errors.ok({})