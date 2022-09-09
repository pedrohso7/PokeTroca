from abc import ABC, abstractclassmethod

class AuthenticateUser(ABC):
  @abstractclassmethod
  def execute(self, socketRequest):
    raise Exception("Should implement method")