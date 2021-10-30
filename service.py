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
color3 = '#cecece' #cinza claro para text box
color4 = '#575757' #cinza

combolist = ['Aguardando','Em Processo','Finalizado'] # LISTA DE FUNÇÕES DA COMBOBOX



############ CRIADOR DA JANELA DE SERVIÇOS ############
def services():
    form = Tk()
    form.title('Tabela de Serviços')
    form.geometry('1000x600')
    form.configure(bg=color1)
    form.resizable(False, False) 
    #SALVA SAPORRA


    def info():
        try:
            itemSelection = app.selection()[0]
            valores=app.item(itemSelection, "values")
            wininfo = Tk()
            wininfo.title('Adicione a Descrição')
            wininfo.geometry('300x450')
            wininfo.configure(bg=color1)
            wininfo.resizable(False, False) 

            lbclient = Label(wininfo,text="Cliente")
            lbclient.grid(row=3, column=1)
            eclient = Label(wininfo,text="", bg=color1)
            eclient.grid(row=4, column=1)

            lbos = Label(wininfo,text="OS")
            lbos.grid(row=5, column=1)
            eos = Label(wininfo,text="", bg=color1)
            eos.grid(row=6, column=1)


            lbstatus = Label(wininfo,text="Status")
            lbstatus.grid(row=7, column=1)
            estatus = Label(wininfo,text="", bg=color1)
            estatus.grid(row=8, column=1)
            
            lbemail = Label(wininfo,text="E-mail")
            lbemail.grid(row=9, column=1)
            eemail = Label(wininfo,text="", bg=color1)
            eemail.grid(row=10, column=1)

            lbdisc = Label(wininfo,text="Descrição")
            lbdisc.grid(row=11, column=1)
            edisc = Label(wininfo,text="", bg=color1)
            edisc.grid(row=12, column=1)


            eclient['text'] = valores[1]
            eos['text'] = valores[0]
            estatus['text'] = valores[2]
            eemail['text'] = valores[3]
            edisc['text'] = valores[4]

        except:
            messagebox.showinfo(title="ERRO", message="Selecione um Serviço")

    
    


    ############ INSERIR ELEMENTOS NA TABELA ############ 
    def insert():
        if vid.get()=="" or vname.get()=="" or vstatus.get()=="" or vmail.get()=="": 
            messagebox.showinfo(title="ERRO", message="Digite todos os dados") 
            return
        app.insert("","end", values=(vid.get(),vname.get(),vstatus.get(),vmail.get()))
        banco_insert()
        vid.delete(0, END)
        vname.delete(0, END)
        vstatus.delete(0, END)
        vmail.delete(0, END)
        vid.focus()
        
    ############ LISTAGEM DE ELEMENTOS DA TABELA ############
    def edit():
        def place():
            try:
                itemSelection = app.selection()[0]
                valores=app.item(itemSelection, "values")
                id=valores[0]
                name=valores[1]
                mail=valores[3]
                comboedit = vedit.get()               
                send_email.email_send(id, name, comboedit, mail)
                vcon = users_db.ConnectDB()
                vquery = "UPDATE tb_users SET T_B_USERSTATUS='"+comboedit+"' WHERE N_OS="+id
                users_db.insert(vcon, vquery)
                winedit.destroy()
                
                
            except:
                messagebox.showinfo(title="ERRO", message="Selecione um Serviço") 

        winedit = Tk()
        winedit.title('Edite o Status')
        winedit.geometry('220x200')
        winedit.configure(bg=color1)
        winedit.resizable(False, False) 
        lbedit = Label(winedit,text="Status")
        vedit = ttk.Combobox(winedit, values=combolist, width=15,justify='center')
        lbedit.place(x=53, y=60)
        vedit.place(x=53, y=80)

        btn_edit = Button(winedit, text='Editar', command=place)
        btn_edit.place(x=53, y=110)

    ############ ADICIONA DESCRIÇÃO AO SERVIÇO SELECIONADO ############
    def description():
        def place_desc():
            try:
                desc = vdesc.get("1.0","end")
                itemSelection = app.selection()[0]
                valores=app.item(itemSelection, "values")
                id=valores[0]
                vcon = users_db.ConnectDB()
                vquery = "UPDATE tb_users SET T_D_DESCRIPTION='"+desc+"' WHERE N_OS="+id
                users_db.insert(vcon, vquery)
                windesc.destroy()
            except:
                messagebox.showinfo(title="ERRO", message="Selecione um Serviço") 

        windesc = Tk()
        windesc.title('Adicione a Descrição')
        windesc.geometry('450x300')
        windesc.resizable(False, False)  
        windesc.configure(bg=color1)
        lbdesc = Label(windesc,text="Descrição")
        vdesc = Text(windesc, width=40, height=5, bg=color3)
        lbdesc.place(x=53, y=60)
        vdesc.place(x=53, y=80)

        btn_desc = Button(windesc, text='Adicionar', command=place_desc)
        btn_desc.place(x=53, y=190)


    

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
    def banco_insert():

        iD = vid.get()
        name = vname.get()
        mail = vmail.get()
        status = vstatus.get()
        vsql =   "INSERT INTO tb_users (N_OS, T_A_USERNAME, T_B_USERSTATUS, T_C_USEREMAIL) VALUES('"+iD+"','"+name+"','"+status+"','"+mail+"')"
        vcon = users_db.ConnectDB()
        users_db.insert(vcon, vsql)
        send_email.email_send(iD, name, status, mail)############ ENVIA AS VARIÁVEIS AO SEND_EMAIL QUE ENVIA O EMAIL PARA O CLIENTE

    


        
    
    ############ CRIANDO A TABELA E SUAS COLUNAS ############
    app = ttk.Treeview(form,columns=('os','cliente','status','email','desc'), show='headings')
    app.column('os', minwidth=0, width=70)
    app.column('cliente', minwidth=0, width=90)
    app.column('status', minwidth=0, width=90)
    app.column('email', minwidth=0, width=250)
    app.column('desc', minwidth=0, width=300)
    app.heading('os', text='OS')
    app.heading('cliente', text='CLIENTE')
    app.heading('status', text='STATUS')
    app.heading('email', text='EMAIL')
    app.heading('desc', text='DESCRIÇÃO')
    app.place(x=100,y=100)
    banco_fill()


    ############ TEXTO E ENTRADA DA ORDEM DE SERVIÇO ############
    lbid = Label(form,text="OS")
    vid = Entry(form, width=10,justify='center')
    vid.place(x=100, y=430)
    lbid.place(x=100, y=410)
    
    ############ TEXTO E ENTRADA DO NOME DO CLIENTE ############
    lbname = Label(form,text="Cliente")
    vname = Entry(form, width=30,justify='center')
    vname.place(x=190, y=430)
    lbname.place(x=190, y=410)

    ############ TEXTO E COMBOBOX DO STATUS DO SERVIÇO ############
    lbstatus = Label(form,text="Status")
    vstatus = ttk.Combobox(form, values=combolist, width=15,justify='center')
    vstatus.place(x=400, y=430)
    lbstatus.place(x=400, y=410)

    ############ TEXTO E ENTRADA DO EMAIL DO CLIENTE ############
    lbmail = Label(form,text="E-mail")
    vmail = Entry(form, width=40,justify='center')
    vmail.place(x=540, y=430)
    lbmail.place(x=540, y=410)



    ############ BOTÃO INSERIR ############
    btn_insert = Button(form, text='Add', command=insert,width=4)
    btn_insert.place(x=800,y=430)

    ############ BOTÃO DELETE ############
    btn_delete = Button(form, text='Del', command=banco_delete,width=4)
    btn_delete.place(x=840,y=430)


    ############ BOTÃO OBTER ############
    btn_edit = Button(form, text='Editar', command=edit)
    btn_edit.place(x=100,y=327)

    ############ BOTÃO REFRESH ############
    btn_refresh = Button(form, text='Atualizar', command=banco_fill)
    btn_refresh.place(x=846,y=327)

    ############ BOTÃO DESCRIÇÃO ############
    btn_description = Button(form, text='Descrição', command=description)
    btn_description.place(x=141,y=327)

    ############ BOTÃO INFORMAÇÃO ############
    btn_description = Button(form, text='Info', command=info)
    btn_description.place(x=203,y=327)

    form.mainloop()

