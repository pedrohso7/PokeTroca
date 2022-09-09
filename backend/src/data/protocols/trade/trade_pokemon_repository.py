from abc import ABC, abstractclassmethod

class TradePokemonRepository(ABC):
  @abstractclassmethod
  def update (self, tradeData):
    raise Exception("Should implement method")