from abc import ABC, abstractclassmethod

class ListUserAccount(ABC):
	@abstractclassmethod
	def get (self, id):
		raise Exception("Should implement method")