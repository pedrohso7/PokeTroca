from src.domain.usecases.user.add_user_account import AddUserAccount as AddUserAccountInterface
from src.data.protocols.user.add_user_account_repository import AddUserAccountRepository

class DbAddUserAccount(AddUserAccountInterface):
  
  def __init__(self, add_user_account_repository):
    self.add_user_account_repository = add_user_account_repository

  def add (self, accountUserData):
    return self.add_user_account_repository.add(accountUserData)