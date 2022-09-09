from abc import ABC, abstractclassmethod

class AddUserAccount(ABC):
  @abstractclassmethod
  def add(self, socketRequest):
    raise Exception("Should implement method")