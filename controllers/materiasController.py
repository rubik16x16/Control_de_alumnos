from models.materia import materia
from models.profesor import profesor

class materiasController:

	def __init__(self):
		self.options={
			0: self.all_materias,
			1: self.add_materia,
			2: self.edit_materia,
			3: self.delete_materia
		}

	def index(self):
		view_options=[
			'visualizar todas las materias',
			'agregar Materia',
			'editar Materia',
			'eliminar Materia'
		]

		for index, value in enumerate(view_options):
			print(str(index)+ '---' +value)

		self.resp= int(input('\n Seleccione una opcion:'))
		print(self.options[self.resp]())

	def all_materias(self):
		view= ''
		materias= materia().all()
		for record in materias:
			view+='----'+record['nombre']+'-----\n'
		if view == '':
			view= '__________Sin registro__________'
		return view
		
	def add_materia(self):
		view=''
		nombre= input('Nombre:')
		profesores= profesor().all()
		view+='___lista de profesores registrados____\n'
		for record in profesores:
			view+='-_______________profesor_______________\n'
			view+='-Nombre:'+record['nombre']+'\n'
			view+='-Apellido:'+record['apellido']+'\n'
			view+='-C.I:'+str(record['ci'])+'\n'
			view+='-_______________________________________\n\n\n'
		print(view)
		profesor_folder= int(input('Escriba el C.I. de algun profesor registrado:'))
		new_profesor= profesor()
		query = new_profesor.find({'ci':profesor_folder})
		if query != None:
			data ={
				'nombre': nombre,
				'profesor_id': new_profesor.attr['id']
				}
			nueva_materia= materia(data)
			nueva_materia.save()
			return 'Materia Agregada'
		return 'Este profesor no esta registrado'

	def edit_materia(self):
		index_folder= input('Campo indice:')
		value= input('Valor:')
		
		edit_folder= input('Campo que desea editar:')
		edit_value= input('Valor:')

		find= {
			index_folder: value
		}

		edit= {
			edit_folder: edit_value
		}

		materia().update(find, edit)
		return 'Actualizacion exitosa!\n'

	def delete_materia(self):
		index_folder= input('\n Campo indice:')
		value= input('\n Valor:')
		query= {
			index_folder: value
		}
		materia().delete(query)
		return 'Eliminacion exitosa!\n'