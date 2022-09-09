from src.domain.usecases.user.list_user_account import ListUserAccount as ListUserAccountInterface

class DbListUserAccount(ListUserAccountInterface):
  
  def __init__(self, list_user_account_repository):
    self.list_user_account_repository = list_user_account_repository

  def get (self, id):
    return self.list_user_account_repository.get(id)