import services.database as db
import models.cliente as cliente

def incluir(cliente):
	
	db.cursor.execute("""
		INSERT INTO Cliente(cliNome, cliIdade, cliProfissao) 
		VALUES (?, ? ,?)""", (cliente.nome, cliente.idade, cliente.profissao))
	db.con.commit()
 
def selecionarById(id):
    db.cursor.execute(f"SELECT * FROM Cliente WHERE id = ?", (id,))
    costumerList = []
    
    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))
    
    return costumerList

# def alterar(cliente):
# 	db.cursor.execute(f"""
# 		UPDATE Cliente
#         SET cliNome = {cliente.nome}, cliIdade = {cliente.idade}, cliProfissao = {cliente.profissao}
#         WHERE id = {cliente.id}
#         """)
# 	db.con.commit()
 
def alterar(cliente):
    db.cursor.execute("""
        UPDATE Cliente
        SET cliNome = ?, cliIdade = ?, cliProfissao = ?
        WHERE id = ?
    """, (cliente.nome, cliente.idade, cliente.profissao, cliente.id))
    db.con.commit()
    
def excluir(id):
    db.cursor.execute(f"""
		DELETE FROM Cliente WHERE id = ? """, (id,))
    db.con.commit()
 
def selecionarTodos():
    db.cursor.execute("SELECT * FROM Cliente")
    costumerList = []
    
    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))
    
    return costumerList
    