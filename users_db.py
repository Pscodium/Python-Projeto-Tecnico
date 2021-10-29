
import sqlite3
from sqlite3 import Error


# conexão com o banco de dados


def ConnectDB():
    way = 'C:\\Users\\Cliente\\Desktop\\DEV\\Python_Senai_Projeto\\programa-empresarial\\work.db'
    con=None
    try:
        con=sqlite3.connect(way)
    
    except Error as ex:
        print(ex)
    return con

vcon = ConnectDB()

#vsql = "INSERT INTO tb_users (T_USERNAME, T_USEREMAIL, T_USERSTATUS) VALUES('"++"','"++"','"++"')"

def insert(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Registro Inserido com SUCESSO')

    except Error as ex:
        print(ex)

#insert(vcon, vsql)
def fill(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        res=c.fetchall()
        vcon.close()
        print('Registros Obtidos com SUCESSO')
    except Error as ex:
        print(ex)
    return res


def delete(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        
        vcon.close()
        print('Registro Removido com SUCESSO')
    except Error as ex:
        print(ex)