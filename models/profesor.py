from .model import model

class profesor(model):

	def __init__(self, data= {}):
		self.attr= data

	def table(self):
		return 'profesores'

	def primary_key(self):
		return 'id'

	def materia(self):
		data= self.has_one({
			'table': 'materias',
			'table_id': 'profesor_id'
			})
		return data