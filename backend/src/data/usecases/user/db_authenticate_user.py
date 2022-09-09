from src.domain.usecases.user.authenticate_user import AuthenticateUser as AuthenticateUserInterface

class DbAuthenticateUser(AuthenticateUserInterface):
  
  def __init__(self, authenticate_user_repository):
    self.authenticate_user_repository = authenticate_user_repository

  def execute (self, userData):
    return self.authenticate_user_repository.execute(userData)