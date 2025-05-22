import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setup_teardown():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_adicionar_localizacao(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.facebook.com/me/")
    input("Faça login e pressione ENTER para continuar...")  # login manual

    driver.get("https://www.facebook.com/me/")
    wait = WebDriverWait(driver, 20)

    # Clica na área para criar uma publicação
    area_de_publicar = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"No que você está pensando") or contains(text(),"pensando")]'))
    )
    area_de_publicar.click()

    # Escreve o texto na caixa de publicação
    caixa_texto = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
    )
    texto_para_postar = "post automatizado"
    caixa_texto.send_keys(texto_para_postar)

    # Espera até o ícone de localização aparecer
    icone_localizacao = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, '//img[contains(@src, "8zlaieBcZ72.png")]'
    ))
    )

    # Clica no botão de localização
    icone_localizacao.click()

#     # Digita o local
#     campo_busca = wait.until(
#         EC.visibility_of_element_located((By.XPATH, '//input[@aria-label="Procurar local"]'))
#     )
#     campo_busca.send_keys("Recife")
#     time.sleep(2)

#     # Seleciona a primeira sugestão
#     primeira_opcao = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '(//ul//span[contains(text(),"Recife")])[1]'))
#     )
#     primeira_opcao.click()
#     time.sleep(2)

#     # Fecha o modal (sem publicar)
#     fechar = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]'))
#     )
#     fechar.click()

#     print("Localização adicionada com sucesso (simulado).")


# def test_denunciar_publicacao(setup_teardown):
#     driver = setup_teardown
#     driver.get("https://www.facebook.com/me/")
#     input("Faça login e pressione ENTER para continuar...")
#     driver.get("https://www.facebook.com/me/")

#     # Esperar o feed carregar
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Mais opções']"))
#     )

#     # Clicar nos três pontinhos da primeira publicação
#     menu_mais_opcoes = driver.find_elements(By.CSS_SELECTOR, "div[aria-label='Mais opções']")[0]
#     menu_mais_opcoes.click()
#     time.sleep(2)

#     # Clicar em "Reportar publicação"
#     reportar = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, "span:contains('Reportar publicação'), div:contains('Reportar publicação')"))
#     )
#     reportar.click()

#     time.sleep(3)
#     # Validação básica (ex: modal de denúncia aberta)
#     assert "Denunciar" in driver.page_source or "Reportar" in driver.page_source

#     print("Fluxo de denúncia de publicação iniciado.")