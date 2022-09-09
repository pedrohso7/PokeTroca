from src.infra.database.sqlite.views.user.user_view import *
from src.data.protocols.user.authenticate_user_repository import AuthenticateUserRepository as AuthenticateUserRepositoryInterface

class AuthenticateUserRepo(AuthenticateUserRepositoryInterface):
  
  def execute (self, userData):
    user_result = authenticate(userData)
    if (user_result == None):
      return None
    user_dict = { 
      "id": user_result[0],
      "username": user_result[1],
      "name": user_result[3]
    }
    return user_dict