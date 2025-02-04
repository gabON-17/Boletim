import mysql.connector
def com_sql(comando=''):  
    conect = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password= '',
        database= 'boletim_registro'
    )
    cursor = conect.cursor()

    cursor.execute(comando)
    conect.commit() # Sempre que modificar o banco tem que usar

    cursor.close()
    conect.close()


def tabela(comando=''):
    conect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'boletim_registro'
    )
    cursor = conect.cursor()
    cursor.execute(comando)

    resultado = cursor.fetchall()

    lista = list()
    for tupla in resultado:
        for valor in tupla:
            lista.append(valor)

    cursor.close()
    conect.close()
    
    return lista
