import tkinter as tk
from tkinter import *
from tkinter import ttk
import users_db
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


############ CORES ############
color1 = '#ffffff' #branco 
color2 = '#000000' #preto
color3 = '#cecece' #cinza claro para text box
color4 = '#575757' #cinza
colorb = '#feb236'  #amarelo Buttons
colorfundo = '#6b5b95' #Roxo fundo
colorentry = '#dbdad5' 
fgtext= 'White'
colortable = '#E6E6FA'

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']


def revenues():

    ########## JANELA ############
    window = tk.Tk()
    window.title("Faturamento")
    window.geometry('700x800')
    window.configure(bg=colorfundo)
    window.resizable(False, False)

    ########## ATUALIZAÇÃO COM O BANCO DE DADOS #########
    def banco_fill():
            app.delete(*app.get_children())
            vquery="SELECT N_OS, T_A_USERNAME, N_DATE, N_VALUE FROM tb_users order by N_OS"
            vcon = users_db.ConnectDB()
            linhas=users_db.fill_fat(vcon, vquery)

            for i in linhas:
                app.insert("","end",values=i)

    ########## INSERINDO/ATUALIZANDO ITENS DENTRO DO BANCO DE DADOS #########
    def commit():
            ######### ENUMERANDO OS MESES PARA A PLANILHA #########
            me = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
            for i in range(12):
                    m = data1.get()
                    if me[i] == m:
                        mesnum = i+1
                        if mesnum<10:
                            mesnum = '0'+str(mesnum)
                        

            if data.get() == '' or data1.get() == '' or data2.get() =='' or value_entry.get() == '':
                    messagebox.showinfo(title="ERRO", message="Digite todos os dados")
                    return
            try:

                itemSelection = app.selection()[0]
                valores = app.item(itemSelection, "values")
                os = valores[0]
                value = value_entry.get()
                dias = data.get()+'/'+data1.get()+'/'+data2.get()
                grafic = data2.get()+'-'+str(mesnum)
                mes = data1.get()
                ano = data2.get()

                

                vcon = users_db.ConnectDB()
                vquery = "UPDATE tb_users SET N_DATE='"+dias+"', N_VALUE='"+value+"' WHERE N_OS="+os
                query = "UPDATE tb_hist SET N_YEAR='"+ano+"', N_DATE='"+grafic+"', N_MONTH='"+mes+"', N_VALUE='"+value+"' WHERE N_OS="+os
                users_db.insert(vcon, vquery)
                users_db.hist(vcon, query)
                banco_fill()


            except:
                messagebox.showinfo(title="ERRO", message="Selecione um Serviço")

    ######### FUNÇÃO PARA SELEÇÃO DE ITENS DO BANCO DE DADOS E CRIAÇÃO DE ARQUIVOS EXCEL COM OS DADOS #########
    def cria_planilha():

        query = "SELECT N_DATE, N_VALUE FROM tb_hist order by N_OS"
        vcon = users_db.ConnectDB()
        lista = users_db.fill(vcon, query)

        dados = pd.DataFrame(list(lista), columns=["Data", "Valor"])
        dados.to_excel("faturamento.xlsx", sheet_name='faturamento', index = False)

    ########## FUNÇÃO DE LEITURA DE ARQUIVO XLSX PARA CRIAÇÃO DO GRÁFICO ##########
    def cria_grafico():
        arquivo = 'faturamento.xlsx'

        dataframe = pd.read_excel(arquivo, sheet_name="faturamento")

        print(dataframe)

        lucro = dataframe.groupby(['Data']).sum()
        total = dataframe['Valor'].sum()

        relatorio_lucro = lucro.loc[:,"Data":"Valor"]

        print(relatorio_lucro)
        total_label['text'] = 'R$'+str(total)

        relatorio_lucro.plot(kind='bar', color=colorfundo)

        plt.gcf().autofmt_xdate()
        plt.grid(True)
        plt.show()



    ######### ESTILO DA JANELA ############
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= colorentry, background= fgtext)


    ########## TABELA ############
    app = ttk.Treeview(window,columns=('os','cliente','data','valor'), show='headings', height=27)
    app.column('os', minwidth=0, width=100)
    app.column('cliente', minwidth=0, width=236)
    app.column('data', minwidth=0, width=220)
    app.column('valor', minwidth=0, width=120)
    app.heading('os', text='OS')
    app.heading('cliente', text='CLIENTE')
    app.heading('data', text='DATA')
    app.heading('valor', text='VALOR')
    app.place(x=10,y=50)

        
    ########## LABEL E ENTRY DO VALOR DO SERVIÇO ##########
    value_label = Label(window,text="Valor", bg=colorfundo, fg=fgtext)
    value_entry = Entry(window, width=10,justify='center', bg=colorentry)
    value_label.place(x=500, y=680)
    value_entry.place(x=500, y=700)

    ########## GERA DIAS E COLOCA 0 NA FRENTE DOS NÚMEROS MENORES QUE 10 #########
    dia = []
    for i in range(1,32):
        if i<10:
            dia.append('0'+str(i))
        else:
            dia.append(i)

    ######### LABEL E COMBOBOX COM O DIA ##########
    dia_label = Label(window,text="Dia", bg=colorfundo, fg=fgtext)
    dia_label.place(x=250, y=680)
    data = ttk.Combobox(window, values=dia, width=5)
    data.place(x=250, y=700)


    ######### LABEL DO VALOR TOTAL ###########
    total_label = Label(window, text='Total', width=8, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Raleway 20 bold'), bg=colorentry, fg=color2)
    total_label.place(x=50, y=680)

    ######### LABEL E COMBOBOX DO MES ##########
    mes_label = Label(window,text="Mês", bg=colorfundo, fg=fgtext)
    mes_label.place(x=310, y=680)
    data1 = ttk.Combobox(window, values=meses, width=7)
    data1.place(x=310, y=700)

    ########## CRIA OS ANOS EM LISTA(SIMPLIFICANDO A EDIÇÃO) #########
    ano = []
    for x in range(2020, 2025):
        ano.append(x)
    
    ########## LABEL E COMBOBOX DO ANO #########
    ano_reverso = list(reversed(ano))
    ano_label = Label(window, text='Ano', bg=colorfundo, fg=fgtext)
    ano_label.place(x=383,y=680)
    data2 = ttk.Combobox(window, values=ano_reverso, width=10)
    data2.place(x=383, y=700)

    ######### BOTÃO ENVIAR ############
    botao_enviar = Button(window,text='Enviar',command=commit, bg=colorb, border=0.8, cursor='hand2')
    botao_enviar.place(x=600, y=699)

    ######### BOTÃO QUE GERA A PLANILHA ATUALIZADA ##########
    botao_fat = Button(window, text="Planilha", command=cria_planilha, bg=colorb, border=0.8, cursor='hand2')
    botao_fat.place(x=10, y=619)

    ######### BOTÃO DO GRÁFICO ##########
    botao_graph = Button(window, text="Gráfico", command=cria_grafico, bg=colorb, border=0.8, cursor='hand2')
    botao_graph.place(x=65, y=619)

    

    banco_fill()
    window.mainloop()
revenues()