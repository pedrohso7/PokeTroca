from abc import ABC, abstractclassmethod

class ListTradeSolicitationsRepository(ABC):
  @abstractclassmethod
  def get (self, id):
    raise Exception("Should implement method")