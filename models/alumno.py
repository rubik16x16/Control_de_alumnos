from .model import model

class alumno(model):

	def __init__(self, data= {}):
		self.attr= data

	def table(self):
		return 'alumnos'

	def primary_key(self):
		return 'id'

	def materias(self):
		data= self.belongs_to_many({
			'pivot_table': 'alumno_materia',
			'pivot_id': 'alumno_id',
			'second_table': 'materias',
			'second_id': 'id',
			'second_pivot_id': 'materia_id'
			})
		return data