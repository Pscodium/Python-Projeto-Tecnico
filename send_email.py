import smtplib
from email import message


############ FUNÇÃO QUE RECEBE AS VÁRIAVEIS DAS ENTRYS ############
def email_send(id, name, status, e_mail):  

    email_body = f"""
    <p>Olá {name}, Tudo bem?</p>
    
    <p>Este E-mail não precisa ser respondido pois</p>
    <p>é uma mensagem de confirmação de serviço.</p>

    <p>Recebemos seu produto</p>
    <p>OS: {id}</p>
    <p>Status: {status}</p>

    <p>Em breve voltaremos com novidades...</p>
    """ ########## TEXTO NO BODY DO EMAIL ############

    ############ CHAMANDO A FUNÇÃO MESSAGE ############
    msg = message.Message()
    msg['Subject'] = 'Serviços de Ferramentaria'
    msg['From'] = 'COLOQUE SEU EMAIL'
    msg['To'] = e_mail
    password = 'COLOQUE SUA SENHA'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    ############ LINKANDO AO GMAIL ############
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    ############ FAZENDO LOGIN UTILIZANDO AS VARIÁVEIS CRIADAS ACIMA ############
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('E-mail Enviado')
