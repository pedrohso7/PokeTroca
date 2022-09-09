from abc import ABC, abstractclassmethod

class AuthenticateUserRepository(ABC):
  @abstractclassmethod
  def execute (self, userData):
    raise Exception("Should implement method")