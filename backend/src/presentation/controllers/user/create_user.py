
from src.domain.usecases.user.add_user_account import AddUserAccount
from src.presentation.errors.errors import Errors

class CreateUserController:
  def __init__ (self, addUserAccount):
    self.addUserAccount = addUserAccount

  def handle (self, socketRequest):
    requiredFields = ['username', 'password', 'name']
  
    for fields in requiredFields:
      if socketRequest[fields] == None:
        return Errors.badRequest(f"Missing {fields} Field")
    result_add_user_account = self.addUserAccount.add(socketRequest)
    if (result_add_user_account != None):
      print(f'Error: {result_add_user_account}')
      return Errors.badRequest(f"E-mail já existente!")
    return Errors.ok({})