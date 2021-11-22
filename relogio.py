import tkinter as tk
from tkinter import *
from datetime import datetime

window = tk.Tk()
window.title('Relógio')
window.geometry('500x300')
window.configure(bg='white')



def relogio():

    tempo=datetime.now()

    hora=tempo.strftime('%H:%M:%S')
    horario.config(text=hora)
    horario.after(200, relogio)



horario = Label(window, text='', font=("Arial 20"), fg='black', bg='white')
horario.grid(row=1, column=1, sticky=NW)



relogio()
window.mainloop()