from .model import model

class alumno_materia(model):

	def __init__(self, data= {}):
		self.attr= data

	def table(self):
		return 'alumno_materia'

	def primary_key(self):
		return 'id'