from abc import ABC, abstractclassmethod

class ListUserInventoryRepository(ABC):
  @abstractclassmethod
  def get (self, id):
    raise Exception("Should implement method")