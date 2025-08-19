from selenium import webdriver
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os



navegador=webdriver.Chrome()

navegador.maximize_window()

navegador.get("https://clone-olx-devaprender.netlify.app/")

list_value=navegador.find_elements(By.XPATH,"//div[@class='mb-2']")

list_modelo=navegador.find_elements(By.XPATH,"//h3[@class='text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]']")


for list_value,list_modelo in zip(list_value,list_modelo):
    
    with open('preços3.csv','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{list_value.text},{list_modelo.text},{os.linesep}')
        
        
remeten


