# 4 Automações com Python que Vão SALVAR Seu Tempo no Trabalho

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



# 1. AUTOMATIZAÇÃO DE E-MAILS

def enviar_email():
    remetente = "pythonimpressionador@gmail.com"
    senha = "twxn dyql fkid afbd"
    destinatario = "pythonimpressionador+diretoria@gmail.com"
    assunto = "Relatório de vendas do dia de hoje"
    corpo = "Este é um email automático do relatório de vendas do dia de hoje. Batemos a meta."
    
     # Anexando o arquivo
    nome_arquivo = "preços.csv"  # Altere para o nome do seu arquivo
    caminho_arquivo = f"./{nome_arquivo}"  # Caminho relativo ou absoluto

    with open(caminho_arquivo, "rb") as anexo:
        parte = MIMEBase("application", "octet-stream")
        parte.set_payload(anexo.read())
        encoders.encode_base64(parte)
        parte.add_header("Content-Disposition", f"attachment; filename={nome_arquivo}")
        mensagem.attach(parte)
        

    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain"))

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, mensagem.as_string())
    servidor.quit()
    print("Email enviado com sucesso")

enviar_email()




# 2. AUTOMATIZAÇÃO DE ARQUIVOS (Renomeação e Organização)
import os

def organizar_arquivos():
    pasta = "./arquivos"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    arquivos_pasta_atual = os.listdir(".")

    for arquivo in arquivos_pasta_atual:
        if ".txt" in arquivo:
            os.rename(arquivo, f"{pasta}/{arquivo}")
    print("ARquivos organizados")

organizar_arquivos()


# 3. AUTOMATIZAÇÃO NO EXCEL (Atualizar uma Planilha)
import openpyxl

def atualizar_planilha():
    workbook = openpyxl.load_workbook("dados.xlsx")
    aba = workbook.active
    aba.append(["Lira", 31, "Programação"])
    workbook.save("dados.xlsx")
    print("Planilha atualizada")

atualizar_planilha()



# 4. AUTOMATIZAÇÃO DE WEB SCRAPING (Extração de Dados da Web)
from bs4 import BeautifulSoup
import requests

def extrair_informacoes_site():
    url = "https://www.nationalgeographic.com/latest-stories"
    headers = {"User-Agent": "Mozilla/5.0"}
    requisicao = requests.get(url, headers=headers)

    if requisicao.status_code == 200:
        pagina = BeautifulSoup(requisicao.text, "html.parser")
        titulos = pagina.find_all(class_="sr-only")
        for titulo in titulos:
            print(titulo.text)

extrair_informacoes_site()