from src.presentation.controllers.user.create_user import CreateUserController
from src.data.usecases.user.db_add_user_account import DbAddUserAccount
from src.infra.database.sqlite.repository.add_user_account_repository.add_user_account import AddUserAccountRepo

class AddUserAccountFactory:
  def makeUserAccountFactory(socketRequest):
    addUserAccountRepo = AddUserAccountRepo()
    dbAddUserAccount = DbAddUserAccount(addUserAccountRepo)
    createUserController = CreateUserController(dbAddUserAccount)
    result = createUserController.handle(socketRequest)
    return result 