from models.profesor import profesor

class profesoresController:

	def __init__(self):
		self.options={
			0: self.find_profesor,
			1: self.all_profesores,
			2: self.add_profesor,
			3: self.edit_profesor,
			4: self.delete_profesor
		}

	def index(self):
		view_options=[
			'buscar profesor(es)',
			'visualizar todos los profesores',
			'agregar profesor',
			'editar profesor(es)',
			'eliminar profesor(es)'
		]

		for index, value in enumerate(view_options):
			print(str(index)+ '---' +value)

		self.resp= int(input('\n Seleccione una opcion:'))
		print(self.options[self.resp]())

	def all_profesores(self):
		view= ''
		profesores= profesor().all()
		for record in profesores:
			nuevo_profesor= profesor()
			nuevo_profesor.find({
				'id': record['id']
				})
			materia= nuevo_profesor.materia()
			if materia != None:
				materia= materia['nombre']
			else:
				materia= 'no tiene materia asignada'
			view+='-_______________profesor_______________\n'
			view+='-Nombre:'+record['nombre']+'\n'
			view+='-Apellido:'+record['apellido']+'\n'
			view+='-C.I:'+str(record['ci'])+'\n'
			view+='-_______________Materia_______________\n'
			view+='--'+materia+'\n'
			view+='-______________________________________\n\n\n'
		if view == '':
			view= '__________Sin registro__________'
		return view

	def find_profesor(self):
		view= '-Sin coincidencias\n'
		index_folder= input('Campo indice:')
		value= input('Valor:')
		query= {
			index_folder: value
		}
		profesores= profesor().find(query)
		if profesores != None:
			view= ''
			for record in profesores:
				nuevo_profesor= profesor()
				nuevo_profesor.find({
					'id': record['id']
					})
				materia= nuevo_profesor.materia()
				view+='-_______________profesor_______________\n'
				view+='-Nombre:'+record['nombre']+'\n'
				view+='-Apellido:'+record['apellido']+'\n'
				view+='-C.I:'+str(record['ci'])+'\n'
				view+='-_______________Materia_______________\n'
				view+='--'+materia['nombre']+'\n'
				view+='-______________________________________\n\n\n'
		return view
		
	def add_profesor(self):
		nombre= input('Nombre:')
		apellido= input('Apellido:')
		ci= int(input('C.I:'))

		data= {
			'nombre': nombre,
			'apellido': apellido,
			'ci': ci
		}

		nuevo_profesor= profesor(data)
		nuevo_profesor.save()

		return 'nuevo profesor agregado'

	def edit_profesor(self):
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

		profesor().update(find, edit)
		return 'Actualizacion exitosa!\n'

	def delete_profesor(self):
		index_folder= input('\n Campo indice:')
		value= input('\n Valor:')
		query= {
			index_folder: value
		}
		profesor().delete(query)
		return 'Eliminacion exitosa!\n'