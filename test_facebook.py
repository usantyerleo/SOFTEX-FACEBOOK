import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from dotenv import load_dotenv
#import os
#from automacao import login
import time

# Carrega as variáveis do arquivo .env
#load_dotenv()
#FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
#FACEBOOK_SENHA = os.getenv("FACEBOOK_SENHA")

# Fixture para abrir e fechar o navegador
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
    input("Faça login e pressione ENTER para continuar...")
    driver.get("https://www.facebook.com/me/")
    wait = WebDriverWait(driver, 10)

    publicar = driver.find_element(By.CSS_SELECTOR, "div[aria-label*='pensando']")
    publicar.click()

    # Esperar a modal abrir
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Adicionar localização']"))
    )

    # Clicar no botão de localização
    botao_localizacao = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Adicionar localização']")
    botao_localizacao.click()

    # Digitar o local
    campo_busca = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Pesquisar locais']"))
    )
    campo_busca.send_keys("Recife")
    time.sleep(2)

    # Selecionar a primeira opção
    primeira_opcao = driver.find_element(By.CSS_SELECTOR, "div[role='option']")
    primeira_opcao.click()
    time.sleep(2)

    # Verificação (opcional): você pode verificar se a localização aparece
    assert "Recife" in driver.page_source

    # Aguarda e fecha o modal sem publicar (opcional)
    fechar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Fechar']")))
    fechar.click()

    print("Localização adicionada com sucesso (simulado).")


def test_denunciar_publicacao(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.facebook.com/me/")
    input("Faça login e pressione ENTER para continuar...")
    driver.get("https://www.facebook.com/me/")

    # Esperar o feed carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Mais opções']"))
    )

    # Clicar nos três pontinhos da primeira publicação
    menu_mais_opcoes = driver.find_elements(By.CSS_SELECTOR, "div[aria-label='Mais opções']")[0]
    menu_mais_opcoes.click()
    time.sleep(2)

    # Clicar em "Reportar publicação"
    reportar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span:contains('Reportar publicação'), div:contains('Reportar publicação')"))
    )
    reportar.click()

    time.sleep(3)
    # Validação básica (ex: modal de denúncia aberta)
    assert "Denunciar" in driver.page_source or "Reportar" in driver.page_source

    print("Fluxo de denúncia de publicação iniciado.")