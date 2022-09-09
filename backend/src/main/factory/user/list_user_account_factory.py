from src.presentation.controllers.user.list_user_account import ListUserAccountController
from src.data.usecases.user.db_list_user_account import DbListUserAccount
from src.infra.database.sqlite.repository.list_user_account_repository.list_user_account import ListUserAccountRepo

class ListUserAccountFactory:
  def makeListUserAccountFactory(socketRequest):
    listUserAccountRepo = ListUserAccountRepo()
    dbListUserAccount = DbListUserAccount(listUserAccountRepo)
    manageUserController = ListUserAccountController(dbListUserAccount)
    result = manageUserController.list(socketRequest)
    return result