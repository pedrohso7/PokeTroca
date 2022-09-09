from abc import ABC, abstractclassmethod

class AddTradeSolicitationsRepository(ABC):
  @abstractclassmethod
  def add (self, tradeSolicitationData):
    raise Exception("Should implement method")