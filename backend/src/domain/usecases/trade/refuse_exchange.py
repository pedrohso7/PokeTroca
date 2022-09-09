from abc import ABC, abstractclassmethod

class RefuseExchange(ABC):
	@abstractclassmethod
	def update (self, id):
		raise Exception("Should implement method")