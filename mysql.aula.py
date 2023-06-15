import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='cdd2023',
    database ='escola_turmac',
)
print(banco)

meucursor = banco.cursor()
pesquisa = 'select * from aluno;'
meucursor.execute(pesquisa)
#fetchall recebe tudo da pesquisa e retorna atraves de uma tupla
resultado = meucursor.fetchall()

for x in resultado:
    print(x)

nome1 = "Mexias Ney"
telefone1 = "11111111"
media1= 7.58
sql = "INSERT INTO aluno (nome, telefone,media) VALUES (%s, %s,%s);"
data = (nome1, telefone1,media1)
meucursor.execute(sql, data)
banco.commit()
userid = meucursor.lastrowid
print(userid)
banco.close()
meucursor.close()
banco.close()