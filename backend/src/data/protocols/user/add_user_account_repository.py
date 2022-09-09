from abc import ABC, abstractclassmethod

class AddUserAccountRepository(ABC):
  @abstractclassmethod
  def add(self, accountUserData):
    raise Exception("Should implement method")