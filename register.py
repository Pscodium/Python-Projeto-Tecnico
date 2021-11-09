import tkinter as tk
import users_db
from tkinter import *
from tkinter import messagebox

color1 = '#ffffff' #branco
color2 = '#6b5b95' #Roxo fundo
color4 = '#feb236' #amarelo Buttons
color5 = '#eb3434' #vermelho
colorentry = '#dbdad5'



def register():
    window = tk.Tk()
    window.title('Cadastro')
    window.geometry('300x275')
    window.configure(bg=color2)


    

    def submit():
        if input_name_user.get() == "" or input_user.get() == "" or input_password.get() == "" or input_mail.get() == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados") 
            return
        banco_insert()
        input_name_user.delete(0, END)
        input_user.delete(0, END)
        input_password.delete(0, END)
        input_mail.delete(0, END)
        window.destroy()


    def banco_insert():
        name = input_name_user.get()
        user = input_user.get()
        password = input_password.get()
        mail = input_mail.get()
        vsql =   "INSERT INTO tb_login (T_name, T_user, T_pass, T_email) VALUES('"+name+"','"+user+"','"+password+"','"+mail+"')"
        vcon = users_db.ConnectDB()
        users_db.insert(vcon, vsql)


    app_name = Label(window, text='Cadastro', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Raleway 16 bold'), bg=color1, fg=color2)
    app_name.grid(column=0, row=0)

    app_line = Label(window, text='', width=300, height=1, padx=0, relief='flat', anchor='center', font=('Raleway 1'), bg=color4, fg=color2)
    app_line.grid(column=0, row=1)


    name_user = Label(window, text='Nome', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color2, fg='white')
    name_user.place(x=10, y=60)

    input_name_user = Entry(window,text='digite seu nome', width=20, relief='solid', font=('Raleway 10 bold'), justify='center', bg=colorentry)
    input_name_user.place(x=80, y=60)

    user = Label(window, text='Usuário', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color2, fg='white')
    user.place(x=10, y=100)

    input_user = Entry(window,text='digite seu usuario', width=20, relief='solid', font=('Raleway 10 bold'), justify='center', bg=colorentry)
    input_user.place(x=80, y=100)

    

    login_password = Label(window, text='Senha', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color2, fg='white')
    login_password.place(x=10, y=140)

    input_password = Entry(window, show='*', text='digite sua senha', width=20, relief='solid', font=('Raleway 10 bold'), justify='center', bg=colorentry)
    input_password.place(x=80, y=140)

    mail = Label(window, text='E-mail', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color2, fg='white')
    mail.place(x=10, y=180)

    input_mail = Entry(window,text='digite seu e-mail', width=20, relief='solid', font=('Raleway 10 bold'), justify='center', bg=colorentry)
    input_mail.place(x=80, y=180)

    register_button = Button(window, command=submit, text='Enviar', width=34, height=1, overrelief=SOLID, relief='raised', border=0, anchor='center', font=('Raleway 10 bold'), bg=color4, fg=color1, cursor='hand2')
    register_button.place(x=10,y=230)




    window.mainloop()