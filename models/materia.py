from .model import model

class materia(model):

	def __init__(self, data= {}):
		self.attr= data

	def table(self):
		return 'materias'

	def primary_key(self):
		return 'id'