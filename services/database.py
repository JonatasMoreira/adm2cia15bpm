import sqlite3



with sqlite3.connect('crud_python.db', check_same_thread=False) as con:
	cursor = con.cursor()
	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS Cliente
		(
			id integer primary key autoincrement,
			cliNome text not null,
			cliIdade integer not null,
			cliProfissao text
		)
		""") 
