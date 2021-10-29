import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlite3 import Error
import users_db
import send_email

############ CORES ############
color1 = '#ffffff' #branco 
color2 = '#000000' #preto

combolist = ['Aguardando','Em Processo','Finalizado'] # LISTA DE FUNÇÕES DA COMBOBOX



############ CRIADOR DA JANELA DE SERVIÇOS ############
def services():
    form = Tk()
    form.title('Tabela de Serviços')
    form.geometry('1000x800')
    form.configure(bg=color1) 
    #SALVA SAPORRA



    ############ INSERIR ELEMENTOS NA TABELA ############ 
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
        
    ############ LISTAGEM DE ELEMENTOS DA TABELA ############
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

    ############ ATUALIZAÇÃO DA TABELA COM O BANCO DE DADOS ############
    def banco_fill():
        app.delete(*app.get_children())
        vquery="SELECT * FROM tb_users order by N_OS"
        vcon = users_db.ConnectDB()
        linhas=users_db.fill(vcon,vquery)
        for i in linhas:
            app.insert("","end",values=i)

    ############ DELETANDO NO DB E NA TABELA ############
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


    ############ INSERINDO INFORMAÇÕES DENTRO DA DATABASE ############
    def banco():

        iD = vid.get()
        name = vname.get()
        mail = vmail.get()
        status = vstatus.get()
        vsql =   "INSERT INTO tb_users (N_OS, T_A_USERNAME, T_B_USERSTATUS, T_C_USEREMAIL) VALUES('"+iD+"','"+name+"','"+status+"','"+mail+"')"
        vcon = users_db.ConnectDB()
        users_db.insert(vcon, vsql)
        send_email.email_send(iD, name, status, mail)############ ENVIA AS VARIÁVEIS AO SEND_EMAIL QUE ENVIA O EMAIL PARA O CLIENTE

    


        
    
    ############ CRIANDO A TABELA E SUAS COLUNAS ############
    app = ttk.Treeview(form,columns=('os','cliente','status','email'), show='headings')
    app.column('os', minwidth=0, width=50)
    app.column('cliente', minwidth=0, width=250)
    app.column('status', minwidth=0, width=200)
    app.column('email', minwidth=0, width=300)
    app.heading('os', text='OS')
    app.heading('cliente', text='CLIENTE')
    app.heading('status', text='STATUS')
    app.heading('email', text='EMAIL')
    app.place(x=100,y=70)
    banco_fill()


    ############ TEXTO E ENTRADA DA ORDEM DE SERVIÇO ############
    lbid = Label(form,text="OS")
    vid = Entry(form, width=10,justify='center')
    vid.place(x=100, y=400)
    lbid.place(x=100, y=380)
    
    ############ TEXTO E ENTRADA DO NOME DO CLIENTE ############
    lbname = Label(form,text="Cliente")
    vname = Entry(form, width=30,justify='center')
    vname.place(x=190, y=400)
    lbname.place(x=190, y=380)

    ############ TEXTO E COMBOBOX DO STATUS DO SERVIÇO ############
    lbstatus = Label(form,text="Status")
    vstatus = ttk.Combobox(form, values=combolist, width=15,justify='center')
    vstatus.place(x=400, y=400)
    lbstatus.place(x=400, y=380)

    ############ TEXTO E ENTRADA DO EMAIL DO CLIENTE ############
    lbmail = Label(form,text="E-mail")
    vmail = Entry(form, width=40,justify='center')
    vmail.place(x=540, y=400)
    lbmail.place(x=540, y=380)




    ############ BOTÃO INSERIR ############
    btn_insert = Button(form, text='Add', command=insert,width=4)
    btn_insert.place(x=800,y=400)

    ############ BOTÃO DELETE ############
    btn_delete = Button(form, text='Del', command=banco_delete,width=4)
    btn_delete.place(x=840,y=400)


    ############ BOTÃO OBTER ############
    btn_get = Button(form, text='Obter', command=get)
    btn_get.place(x=544,y=800)

    form.mainloop()

