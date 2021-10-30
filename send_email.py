import smtplib
from email import message
from password import senha


############ FUNÇÃO QUE RECEBE AS VÁRIAVEIS DAS ENTRYS ############
def email_send(iD, name, status, e_mail):  

    
    

    def email_wait():  
        ########## TEXTO NO BODY DO EMAIL ############
        email_body = f"""
        <p>Olá {name}, Tudo bem?\nEste E-mail não precisa ser respondido \npois é uma mensagem de confirmação de serviço.</p>

       <p>Recebemos seu produto</p>
        <p>OS: {iD}</p>
        <p>Status do seu pedido: {status}</p>
        """

        ############ CHAMANDO A FUNÇÃO MESSAGE ############
        msg = message.Message()
        msg['Subject'] = f'Serviços de Ferramentaria - OS-{iD} Aguardando'
        msg['From'] = 'pythondevemailtest@gmail.com'
        msg['To'] = e_mail
        password = senha
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_body)

        ############ LINKANDO AO GMAIL ############
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        ############ FAZENDO LOGIN UTILIZANDO AS VARIÁVEIS CRIADAS ACIMA ############
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('E-mail Enviado')


    def email_process():  
        ########## TEXTO NO BODY DO EMAIL ############
        email_body = f"""
        <p>Olá {name}, Tudo bem?\nEste E-mail não precisa ser respondido \npois é uma mensagem de confirmação de serviço.</p>

       <p>Recebemos seu produto</p>
        <p>OS: {iD}</p>
        <p>Status do seu pedido: {status}</p>

       
        """

        ############ CHAMANDO A FUNÇÃO MESSAGE ############
        msg = message.Message()
        msg['Subject'] = f'Serviços de Ferramentaria - OS-{iD} Em Processo'
        msg['From'] = 'pythondevemailtest@gmail.com'
        msg['To'] = e_mail
        password = senha
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_body)

        ############ LINKANDO AO GMAIL ############
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        ############ FAZENDO LOGIN UTILIZANDO AS VARIÁVEIS CRIADAS ACIMA ############
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('E-mail Enviado')

    def email_finish():  
        ########## TEXTO NO BODY DO EMAIL ############
        email_body = f"""
        <p>Olá {name}, Tudo bem?\nEste E-mail não precisa ser respondido \npois é uma mensagem de confirmação de serviço.</p>

        <p>Recebemos seu produto</p>
        <p>OS: {iD}</p>
        <p>Status do seu pedido: {status}</p>
        """

        ############ CHAMANDO A FUNÇÃO MESSAGE ############
        msg = message.Message()
        msg['Subject'] = f'Serviços de Ferramentaria - OS-{iD} Finalizado'
        msg['From'] = 'pythondevemailtest@gmail.com'
        msg['To'] = e_mail
        password = senha
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_body)

        ############ LINKANDO AO GMAIL ############
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        ############ FAZENDO LOGIN UTILIZANDO AS VARIÁVEIS CRIADAS ACIMA ############
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('E-mail Enviado')


    if status == 'Aguardando':
        email_wait()
    elif status == 'Em Processo':
        email_process()
    elif status == 'Finalizado':
        email_finish()