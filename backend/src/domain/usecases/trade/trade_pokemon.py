from abc import ABC, abstractclassmethod

class TradePokemon(ABC):
	@abstractclassmethod
	def update (self, tradeData):
		raise Exception("Should implement method")