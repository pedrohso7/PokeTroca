from abc import ABC, abstractclassmethod

class ListUserAccountRepository(ABC):
  @abstractclassmethod
  def get (self, id):
    raise Exception("Should implement method")