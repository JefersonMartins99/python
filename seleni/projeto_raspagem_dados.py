from selenium import webdriver
from selenium.webdriver.common.by import By
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import time 
import smtplib 
import os


navegador=webdriver.Chrome()

navegador.maximize_window()

navegador.get("https://clone-olx-devaprender.netlify.app/")

valores_cell=navegador.find_elements(By.XPATH,"//div[@class='mb-2']")

modelos_cell=navegador.find_elements(By.XPATH,"//h3[@class='text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]']")


for valores_cell,modelos_cell in zip (valores_cell,modelos_cell):
    
    with open ('preços2.csv','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{valores_cell.text},{modelos_cell.text},{os.linesep}') 
        

import pandas as pd

df=pd.read_csv("C:/Users/evely/Documents/estudos/python/preços2.csv" , names=["Preço", "Modelo"])

print(df)

            
#Caminho do seu arquivo CSV
caminho_csv = "C:/Users/evely/Documents/estudos/python/preços2.csv"

# Configurações do e-mail
email_origem = "jm4642294@gmail.com"
senha = "lzqq uuen vdhp xijw"  # use senha de app (não a senha normal)
email_destino = "jefersonmartins99@hotmail.com"
assunto="Relatório de Preços e Modelos"
# Cria o corpo da mensagem
mensagem = MIMEMultipart()
mensagem["From"] = email_origem
mensagem["To"] = email_destino
mensagem["Subject"] = assunto

# Corpo do e-mail em texto
corpo_email = "Segue em anexo o DataFrame com preços e modelos."
mensagem.attach(MIMEText(corpo_email, "plain"))

# Anexa o CSV
with open(caminho_csv, "rb") as arquivo:
    parte = MIMEBase("application", "octet-stream")
    parte.set_payload(arquivo.read())

encoders.encode_base64(parte)
parte.add_header("Content-Disposition", f"attachment; filename=precos.csv")
mensagem.attach(parte)

# Conexão com o servidor SMTP do Gmail

servidor = smtplib.SMTP("smtp.gmail.com", 587)
servidor.starttls()
servidor.login(email_origem, senha)
servidor.send_message(mensagem)
servidor.quit()
print("E-mail enviado com sucesso!")


        
            
        

        




