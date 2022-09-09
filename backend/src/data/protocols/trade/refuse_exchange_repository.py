from abc import ABC, abstractclassmethod

class RefuseExchangeRepository(ABC):
  @abstractclassmethod
  def update (self, id):
    raise Exception("Should implement method")