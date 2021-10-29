import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import users_db


color1 = '#ffffff'
color2 = '#000000'





def services():
    form = Tk()
    form.title('Tabela de Serviços')
    form.geometry('1000x800')
    form.configure(bg=color1) 
    #SALVA SAPORRA




    def insert():
        if vid.get()=="" or vname.get()=="" or vstatus.get()=="" or vmail.get()=="": 
            messagebox.showinfo(title="ERRO", message="Digite todos os dados") 
            return
        app.insert("","end", values=(vid.get(),vname.get(),vstatus.get(),vmail.get()))
        banco()
        vid.delete(0, END)
        vname.delete(0, END)
        vstatus.delete(0, END)
        vmail.delete(0, END)
        vid.focus()


    def get():
        try:
            itemSelection = app.selection()[0]
            valores=app.item(itemSelection, "values")
            print("Nome do cliente..: ",valores[1])
            print("Ordem de Serviço.: ",valores[0])
            print("Status do Serviço: ",valores[2])
            print("E-mail do Cliente: ",valores[3])

            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um Serviço a ser mostrado") 


    def banco_fill():
        app.delete(*app.get_children())
        vquery="SELECT * FROM tb_users order by N_OS"
        vcon = users_db.ConnectDB()
        linhas=users_db.fill(vcon,vquery)
        for i in linhas:
            app.insert("","end",values=i)


    def banco_delete():
        itemSelection = app.selection()[0]
        valores=app.item(itemSelection, "values")
        id=valores[0]
        vcon = users_db.ConnectDB()
        try:
            vquery="DELETE FROM tb_users WHERE N_OS="+id
            users_db.delete(vcon,vquery)
        except:
            messagebox.showinfo(title='ERRO', message="Erro ao deletar")
            return
        app.delete(itemSelection)



    def banco():

        iD = vid.get()
        name = vname.get()
        mail = vmail.get()
        status = vstatus.get()
        vsql =   "INSERT INTO tb_users (N_OS, T_A_USERNAME, T_B_USERSTATUS, T_C_USEREMAIL) VALUES('"+iD+"','"+name+"','"+status+"','"+mail+"')"
        vcon = users_db.ConnectDB()
        users_db.insert(vcon, vsql)

    


        
    

    app = ttk.Treeview(form,columns=('os','cliente','status','email'), show='headings')
    app.column('os', minwidth=0, width=50)
    app.column('cliente', minwidth=0, width=250)
    app.column('status', minwidth=0, width=200)
    app.column('email', minwidth=0, width=300)
    app.heading('os', text='OS')
    app.heading('cliente', text='CLIENTE')
    app.heading('status', text='STATUS')
    app.heading('email', text='EMAIL')
    app.grid(column=1,row=5,columnspan=4,pady=5)
    banco_fill()
    #nome do cliente
    #serviço prestado/ordem de serviço
    #email do cliente
    #status do processo



    lbid = Label(form,text="OS")
    vid = Entry(form, width=10,justify='center')
    lbid.grid(column=1, row=0,sticky='w')
    vid.grid(column=1, row=1,sticky='w')
    
    lbname = Label(form,text="Cliente")
    vname = Entry(form, width=30,justify='center')
    lbname.grid(column=2, row=0,sticky='w')
    vname.grid(column=2, row=1,sticky='w')

    lbstatus = Label(form,text="Status")
    vstatus = Entry(form, width=30,justify='center')
    lbstatus.grid(column=3, row=0,sticky='w')
    vstatus.grid(column=3,row=1,sticky='w')

    lbmail = Label(form,text="E-mail")
    vmail = Entry(form, width=30,justify='center')
    lbmail.grid(column=4, row=0,sticky='w')
    vmail.grid(column=4, row=1,sticky='w')




    #botões
    btn_insert = Button(form, text='Inserir', command=insert)
    btn_insert.grid(column=1, row=6, pady=10)


    btn_delete = Button(form, text='Deletar', command=banco_delete)
    btn_delete.grid(column=2, row=6, pady=10)


    btn_get = Button(form, text='Obter', command=get)
    btn_get.grid(column=3, row=6, pady=10)


    form.mainloop()

