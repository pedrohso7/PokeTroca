from src.presentation.errors.errors import Errors

class TradePokemonController:
  def __init__ (self, tradePokemon):
    self.tradePokemon = tradePokemon

  def handle (self, socketRequest):
    requiredFields = ['id']
  
    for fields in requiredFields:
      if socketRequest[fields] == None:
        return Errors.badRequest(f"Missing {fields} Field")
    self.tradePokemon.update(socketRequest["id"])
    return Errors.ok({})