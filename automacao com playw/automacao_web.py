
from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()
    # abrir o navegador
    pagina = contexto.new_page()

    # navegar para uma página
    pagina.goto("https://www.hashtagtreinamentos.com/")

    # pegar infos da página
    print(pagina.title())

    # selecionar um elemento na tela
    # 1ªforma: xpath
    # pagina.locator('xpath=/html/body/main/section[1]/div[2]/a').click()
    # 2ªforma: get_by
    botao = pagina.locator("div").filter(has_text="Torne-se uma referência no").get_by_role("link")
    with contexto.expect_page() as pagina2_info:
        botao.click()

    # selecionar varios elementos
    # links = pagina.get_by_role("link").all()
    # for link in links:
    #     print(link)
    
    # nova página em branco
    # pagina2 = contexto.new_page()

    # nova página -> criar contextos e depois:
    pagina2 = pagina2_info.value
    pagina2.goto("https://www.hashtagtreinamentos.com/comunidade-impressionadora")

    
    
    
    
    

     
    
    time.sleep(4)
    
    
    
    
    
    
    
    
    