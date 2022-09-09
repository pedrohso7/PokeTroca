from src.presentation.errors.errors import Errors

class AddTradeSolicitationsController:
  def __init__ (self, addTradeSolicitations):
    self.addTradeSolicitations = addTradeSolicitations

  def handle (self, socketRequest):
    requiredFields = ['received_user_id', 'sender_user_id', 'want_pokemon_id', 'give_pokemon_id']
  
    for fields in requiredFields:
      if socketRequest[fields] == None:
        return Errors.badRequest(f"Missing {fields} Field")
    self.addTradeSolicitations.add(socketRequest)
    return Errors.ok({})