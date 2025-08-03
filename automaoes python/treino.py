import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email():
    
    remetente="jm4642294@gmail.com"
    senha="nopd yrwk fifi vonb"
    destinatario="jefersonmartins99@hotmail.com"
    assunto="Resumos dos livros"
    corpo="dsada sjahdbahbsda  dashd bha ahd sja hsbdhasjdabs  ajsb dhasb jdash hjdsb has dabshd asbd as abs djabhdadjabd adsah bhab hdsadbhashbdhd sbd hsab dhsa bdh asdhasb dhasb dhasdhasb dhsabhdb asjdnas asn dnas dnas d jnsdandjk and "


    mensagem=MIMEMultipart()

    mensagem["From"]=remetente
    mensagem["To"]=destinatario
    mensagem["Subject"]=assunto
    mensagem.attach(MIMEText(corpo,"plain"))


    servidor=smtplib.SMTP("smtp.gmail.com",587)
    servidor.starttls()
    servidor.login(remetente,senha)
    servidor.sendmail(remetente,destinatario,mensagem.as_string())
    servidor.quit()

    print("Email enviado com sucesso!")

enviar_email()
