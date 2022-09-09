from abc import ABC, abstractclassmethod

class ListUserInventory(ABC):
	@abstractclassmethod
	def get (self, id):
		raise Exception("Should implement method")