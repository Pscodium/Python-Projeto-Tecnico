
import sqlite3
from sqlite3 import Error
from tkinter import messagebox



############ FUNÇÃO QUE FAZ A CONEXÃO COM O BANCO DE DADOS ############
def ConnectDB():
    way = 'D:\\oscorp-service-manager-python-main\\work.db'
    con=None
    try:
        con=sqlite3.connect(way)
    
    except Error as ex:
        print(ex)
    return con

vcon = ConnectDB()


############ FUNÇÃO QUE INSERE INFORMAÇÕES AO BANCO DE DADOS ############
def insert(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Registro Inserido com SUCESSO')

    except Error as ex:
        print(ex)


############ FUNÇÃO QUE INSERE INFORMAÇÕES AO HISTÓRICO ############
def hist(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Registro Inserido com SUCESSO')

    except Error as ex:
        print(ex)



############ FUNÇÃO QUE LINKA A TABELA AO BANCO DE DADOS ############
def fill(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        res=c.fetchall()
        vcon.close()
        print('Registros Atualizados com SUCESSO')
    except Error as ex:
        print(ex)
    return res

def fill_fat(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        res=c.fetchall()
        vcon.close()
        print('Registros Atualizados com SUCESSO')
    except Error as ex:
        print(ex)
    return res


############ FUNÇÃO QUE DELETA INFORMAÇÕES DA DATABASE ############
def delete(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        
        vcon.close()
        print('Registro Removido com SUCESSO')
    except Error as ex:
        print(ex)

def login(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        res=c.fetchone()
        vcon.close()
        print('Procurando usuários')
    except Error as ex:
        print(ex)
    return res
