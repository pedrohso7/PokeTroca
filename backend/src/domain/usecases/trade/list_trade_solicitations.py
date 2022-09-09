from abc import ABC, abstractclassmethod

class ListTradeSolicitations(ABC):
	@abstractclassmethod
	def get (self, id):
		raise Exception("Should implement method")