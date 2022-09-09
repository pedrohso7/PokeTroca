
from src.presentation.errors.errors import Errors

class AuthenticateUserController:
  def __init__ (self, authenticateUser):
    self.authenticateUser = authenticateUser

  def handle (self, socketRequest):
    requiredFields = ['username', 'password']

    for fields in requiredFields:
      if socketRequest[fields] == None:
        return Errors.badRequest(f"Campo {fields} não enviado!")
    user_data = self.authenticateUser.execute(socketRequest)
    print('user data', user_data)
    if (user_data == None):
      return Errors.badRequest("Usuario inexistente!")
    return Errors.ok(user_data)