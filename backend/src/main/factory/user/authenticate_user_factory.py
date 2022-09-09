from src.infra.database.sqlite.repository.authenticate_user_repository.authenticate_user import AuthenticateUserRepo
from src.data.usecases.user.db_authenticate_user import DbAuthenticateUser
from src.presentation.controllers.user.authenticate_user import AuthenticateUserController

class AuthenticateUserFactory:
  def makeAuthenticateUserFactory(socketRequest):
    authenticateUserRepo = AuthenticateUserRepo()
    dbAuthenticateUser = DbAuthenticateUser(authenticateUserRepo)
    authenticateUserController = AuthenticateUserController(dbAuthenticateUser)
    result = authenticateUserController.handle(socketRequest)
    return result