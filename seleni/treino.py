#Varrendo dados com selenium
from selenium import webdriver
#By(Nós permite necontrar elementos )
from selenium.webdriver.common.by import By 
#os(quebra as linhas)
import os

import time


navegador=webdriver.Chrome()

navegador.get("https://clone-olx-devaprender.netlify.app/")

navegador.maximize_window()

time.sleep(5)

#XPATH(Identificador de elementos na tela)

nome_produtos=navegador.find_elements(By.XPATH,"//h3[@class='text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]']")

preco_produtos=navegador.find_elements(By.XPATH,"//span[@class='text-2xl font-bold text-gray-900']")

#for(pra guardar as infomaçoes em um texto)
for nome_produtos,preco_produtos in zip(nome_produtos,preco_produtos):
    
    #criar um arquivo , a letra 'a' de apendde pra adicionar as info.
    with open('preços.csv','a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome_produtos.text},{preco_produtos.text},{os.linesep}')
            








input('')


