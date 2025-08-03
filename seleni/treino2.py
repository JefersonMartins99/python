import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

def enviar_email():

    remetente="jm4642294@gmail.com"
    senha="bhpb emvp izkw jtwp"
    destinatario="jefersonmartins99@hotmail.com"
    assunto ="História de Pernambuco"
    corpo="A História de Pernambuco diz respeito à trajetória histórica do estado brasileiro de Pernambuco. Os primeiros vestígios de ocupação humana no atual território pernambucano possuem cerca de 11 mil anos e se encontram nas regiões de Chã do Caboclo e Furna do Estrago. Os primeiros grupos indígenas a habitar o estado foram os da tradição cultural Itaparica e os Cariris velhos. No período de chegada dos portugueses ao Brasil, o litoral de Pernambuco era habitado pelos caetés e os tabajaras. Muitos estudiosos afirmam que a descoberta do Brasil ocorreu em 26 de janeiro de 1500 quando o navegador espanhol Vicente Yáñez Pinzón desembarcou no Cabo de Santo Agostinho. Mas, ainda que esta tenha sido a viagem mais antiga ao território que atualmente é o Brasil, a Espanha não reivindicou a descoberta por causa do Tratado de Tordesilhas."

    mensagem=MIMEMultipart()
    mensagem["From"]=remetente
    mensagem["To"]=destinatario
    mensagem["Subject"]=assunto
    mensagem.attach(MIMEText(corpo,"plain"))



    nome_arquivo="preços.csv"
    caminho_arquivo=r"C:\Users\evely\Downloads\paython\python projetos\seleni\preços.csv"

    with open(caminho_arquivo,"rb") as anexo:
        parte=MIMEBase("application","octet-stream")
        parte.set_payload(anexo.read())
        encoders.encode_base64(parte)
        parte.add_header("Content-Disposition", f"attachment; filename={nome_arquivo}")
        mensagem.attach(parte)
        
        
        
    servidor=smtplib.SMTP("smtp.gmail.com",587)
    servidor.starttls()
    servidor.login(remetente,senha)
    servidor.sendmail(remetente,destinatario,mensagem.as_string())
    servidor.quit()
    
    print("email enviado com sucesso !")
    
enviar_email()