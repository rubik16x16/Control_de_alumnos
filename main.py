import os
from controllers.alumnosController import alumnosController
from controllers.profesoresController import profesoresController
from controllers.materiasController import materiasController

print('Seleccione una de las opciones:')

view_options=['alumnos', 'profesores', 'materias']

options={
	0: alumnosController().index,
	1: profesoresController().index,
	2: materiasController().index,
}

for index, value in enumerate(view_options):
	print(str(index)+'---' +value)

resp= int(input('\n Seleccione una opcion:'))

options[resp]()

#os.system('cls')