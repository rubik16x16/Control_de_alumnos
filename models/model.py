import json

class model:

	def __init__():
		pass

	def table(self):
		pass

	def prymaryKey():
		pass

	def all(self):
		with open('tables/' +self.table()+ '.data', 'r') as file:
			data= file.read()
		data= json.loads(data)
		return data[self.table()]

	def save(self):
		with open('tables/' +self.table()+ '.data', 'r') as file:
			data= file.read()
		data= json.loads(data)
		table= data[self.table()]
		id_folder= 0
		if len(table) > 0:
			for record in table:
				if record[self.primary_key()] > id_folder:
					id_folder= record[self.primary_key()]
		id_folder+= 1
		self.attr[self.primary_key()]= id_folder
		data[self.table()].append(self.attr)
		data= json.dumps(data)
		with open('tables/' +self.table()+ '.data', 'w') as file:
			file.write(data)
		return id_folder

	#metodo para buscar registros

	def find(self, find):
		query= []
		with open('tables/' +self.table()+ '.data', 'r') as file:
			data= file.read()
		data= json.loads(data)
		table= data[self.table()]
		for record in table:
			found= False
			for key, value in find.items():
				if record[key] != value:
					found= True
					continue
			if found == False:
				query.append(record)
		if len(query) > 0:
			self.attr= query[0]
			return query
		return None

	def delete(self, delete):
		with open('tables/' +self.table()+ '.data', 'r') as file:
			data= file.read()
		table= json.loads(data)
		del_table= json.loads(data)
		for record in table[self.table()]:
			found= False
			for key, value in delete.items():
				if record[key] != value:
					found= True
					continue
			if found == False:
				del_table[self.table()].remove(record)
		with open('tables/' +self.table()+ '.data', 'w') as file:
			file.write(json.dumps(del_table))

	def update(self, find , replace):
		with open('tables/' +self.table()+ '.data', 'r') as file:
			data= file.read()
		table= json.loads(data)
		for record in table[self.table()]:
			found= False
			for key, value in find.items():
				if record[key] != value:
					found= True
					continue
			if found == False:
				for key, value in replace.items():
					record[key]= value
		with open('tables/' +self.table()+ '.data', 'w') as file:
			file.write(json.dumps(table))

	def has_many(self, id_folder, table):
		pass

	def has_one(self, config):
		with open('tables/' +config['table']+ '.data', 'r') as file:
			data= file.read()
		data= json.loads(data)
		table= data[config['table']]
		for record in table:
			if record[config['table_id']] == self.attr['id']:
				return record
		return None


	def belongs_to():
		pass

	def belongs_to_many(self , config):
		with open('tables/' +config['pivot_table']+ '.data', 'r') as file:
			data= file.read()
		data= json.loads(data)
		table= data[config['pivot_table']]
		query=[]
		for record in table:
			if record[config['pivot_id']] == self.attr['id']:
				query.append(record)
		with open('tables/' +config['second_table']+ '.data', 'r') as file:
			data= file.read()
		data= json.loads(data)
		table= data[config['second_table']]
		new_query= []
		for record in query:
			for materia_record in table:
				if materia_record[config['second_id']]== record[config['second_pivot_id']]:
					new_query.append(materia_record)
		return new_query
