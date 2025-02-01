def com_sql(comando=''):
    import mysql.connector

    conect = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password= '',
        database= 'boletim_registro'
    )
    cursor = conect.cursor()

    cod_sql = comando
    cursor.execute(cod_sql)
    conect.commit() # Sempre que modificar o banco tem que usar

    cursor.close()
    conect.close()

