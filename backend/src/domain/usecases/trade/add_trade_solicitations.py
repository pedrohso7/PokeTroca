from abc import ABC, abstractclassmethod

class AddTradeSolicitations(ABC):
	@abstractclassmethod
	def add (self, tradeSolicitationData):
		raise Exception("Should implement method")