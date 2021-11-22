import tkinter as tk
from tkinter import *
from service import services
from register import register
import users_db
from tkinter import messagebox





color1 = '#ffffff' #branco
color2 = '#6b5b95' #Roxo fundo
color4 = '#feb236' #amarelo Buttons
color5 = '#eb3434' #vermelho
colorentry = '#dbdad5'



# CRIANDO A JANELA
window = tk.Tk()
window.title('Janela')
window.geometry('300x200')
window.configure(bg=color1)
window.resizable(False, False) 



############ QUANDO VOCÊ ESCREVER O USER E SENHA CORRETOS, ESTA FUNÇÃO VAI DESTRUIR A JANELA DE LOGIN E ABRIR A TABLE DE SERVIÇOS ############
def login_sucess():
    try:
        user = input_user.get()
        password = input_password.get()
        vquery="SELECT * FROM tb_login WHERE T_user='"+user+"' AND T_pass='"+password+"'"
        vcon = users_db.ConnectDB()
        login = users_db.login(vcon,vquery)
        if login:
            #messagebox.showinfo(title="ERRO", message="Sucesso")
            window.destroy()
            services()
        else:
            messagebox.showinfo(title="ERRO", message="Usuário ou Senha incorretos")
        
        
    

    except:
        messagebox.showinfo(title="ERRO", message="Usuário ou Senha incorretos")






############ DIVIDINDO A TELA EM DOIS ############
window_up_frame = Frame(window, width=300, height=50, bg=color2, pady=0, padx=0, relief='flat')
window_up_frame.grid(row=0, column=0, sticky=NSEW)

window_down_frame = Frame(window, width=300, height=150, bg=color2, pady=0, padx=0, relief='flat')
window_down_frame.grid(row=1, column=0, sticky=NSEW)


app_name = Label(window_up_frame, text='Login Painel', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Raleway 16 bold'), bg=color1, fg=color2)
app_name.place(x=0, y=0)

app_line = Label(window_up_frame, text='', width=300, height=1, padx=0, relief='flat', anchor='center', font=('Raleway 1'), bg=color4, fg=color2)
app_line.place(x=0, y=30)



############ LABELS DE LOGIN E SENHA ############
login_user = Label(window_down_frame, text='Usuário', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color2, fg='white')
login_user.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

input_user = Entry(window_down_frame,text='digite seu usuário', width=20, relief='solid', font=('Raleway 10 bold'), justify='center', bg=colorentry)
input_user.grid(row=1, column=2, sticky=NSEW, pady=10, padx=3)

login_password = Label(window_down_frame, text='Senha', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color2, fg='white')
login_password.grid(row=2, column=1, sticky=NSEW, pady=10, padx=3)

input_password = Entry(window_down_frame, show='*', text='digite sua senha', width=20, relief='solid', font=('Raleway 10 bold'), justify='center', bg=colorentry)
input_password.grid(row=2, column=2, sticky=NSEW, pady=10, padx=3)




############ BOTÃO DE ENTRADA ############
result_button = Button(window_down_frame, command=login_sucess, text='Login', width=34, height=1, overrelief=SOLID, relief='raised', border=0, anchor='center', font=('Raleway 10 bold'), bg=color4, fg=color1, cursor='hand2')
result_button.grid(row=4, column=0, sticky=NSEW, pady=30, padx=10, columnspan=60)

register_button = Button(window_down_frame, command=register, text='Crie uma conta', activebackground=color2, width=24, height=1, overrelief=SOLID, relief='raised', border=0, anchor='center', font=('Raleway 8 bold'), bg=color2, fg=color1, cursor='hand2')
register_button.place(x=20,y=74)


window.mainloop()
