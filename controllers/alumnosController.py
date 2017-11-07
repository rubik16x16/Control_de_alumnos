from models.alumno import alumno
from models.materia import materia
from models.alumno_materia import alumno_materia

class alumnosController:

	def __init__(self):
		self.options={
			0: self.find_alumno,
			1: self.all_alumnos,
			2: self.add_alumno,
			3: self.edit_alumno,
			4: self.delete_alumno
		}

	def index(self):
		view_options=[
			'buscar alumno(s)',
			'visualizar todos los alumnos',
			'agregar alumno',
			'editar alumno(s)',
			'eliminar alumno(s)'
		]

		for index, value in enumerate(view_options):
			print(str(index)+ '---' +value)

		self.resp= int(input('Seleccione una opcion:'))
		print(self.options[self.resp]())

	def all_alumnos(self):
		view= ''
		alumnos= alumno().all()
		for record in alumnos:
			nuevo_alumno= alumno()
			nuevo_alumno.find({
				'id': record['id']
				})
			materias= nuevo_alumno.materias()
			view+='-_______________Alumno_______________\n'
			view+='-Nombre:'+record['nombre']+'\n'
			view+='-Apellido:'+record['apellido']+'\n'
			view+='-Grado:'+record['grado']+'\n'
			view+='-Seccion:'+record['seccion']+'\n'
			view+='-C.I:'+str(record['ci'])+'\n'
			view+='-_______________Materias_______________\n'
			for new_record in materias:
				view+='--'+new_record['nombre']+'\n'
			view+='-______________________________________\n\n\n'
		if view == '':
			view= '__________Sin registro__________'
		return view

	def find_alumno(self):
		view= '-Sin coincidencias\n'
		index_folder= input('Campo indice:')
		value= input('Valor:')
		query= {
			index_folder: value
		}
		alumnos= alumno().find(query)
		if alumnos != None:
			view= ''
			for record in alumnos:
				nuevo_alumno= alumno()
				nuevo_alumno.find({
					'id': record['id']
					})
				materias= nuevo_alumno.materias()
				view+='-_______________Alumno_______________\n'
				view+='-Nombre:'+record['nombre']+'\n'
				view+='-Apellido:'+record['apellido']+'\n'
				view+='-Grado:'+record['grado']+'\n'
				view+='-Seccion:'+record['seccion']+'\n'
				view+='-C.I:'+str(record['ci'])+'\n'
				view+='-_______________Materias_______________\n'
				for new_record in materias:
					view+='--'+new_record['nombre']+'\n'
				view+='-______________________________________\n\n\n'
		return view
		
	def add_alumno(self):
		view= ''
		nombre= input('Nombre:')
		apellido= input('Apellido:')
		grado= input('Grado:')
		seccion= input('Seccion:')
		cedula= int(input('Cedula:'))

		alumno_data= {
			'nombre': nombre,
			'apellido': apellido,
			'grado': grado,
			'seccion': seccion,
			'ci': cedula
		}

		nuevo_alumno= alumno(alumno_data)
		alumno_id= nuevo_alumno.save()

		view+='-_____________Materias Disponibles_____________\n'
		materias= materia().all()
		for record in materias:
			view+='-'+record['nombre']+'\n'
		print(view)
		view= '________________________________________________\n'
		materias= input('inscriba las materias asignadas sin espacios y separadas por ","')
		nueva_materia= ''
		nuevas_materias=[]
		for record in materias:
			if record != ',':
				nueva_materia+= record
			else:
				nuevas_materias.append(nueva_materia)
				nueva_materia=''
		nuevas_materias.append(nueva_materia)
		for record in nuevas_materias:
			materia_record = materia().find({
				'nombre': record
				})
			if materia_record != None:
				materia_id= materia_record[0]['id']
				materia_data={
					'alumno_id': alumno_id,
					'materia_id': materia_id
				}
				nuevo_alumno_materia= alumno_materia(materia_data)
				nuevo_alumno_materia.save()
				view+= '-materia:'+record+' agregada\n'
			else:
				view+= '-materia:'+record+' no esta registrada\n'
		view+='-nuevo alumno agregado\n'
		return view

	def edit_alumno(self):
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

		alumno().update(find, edit)
		return 'Actualizacion exitosa!\n'

	def delete_alumno(self):
		index_folder= input('Campo indice:')
		value= input('Valor:')
		query= {
			index_folder: value
		}
		alumno().delete(query)
		return 'Eliminacion exitosa!\n'