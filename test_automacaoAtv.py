from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setup_teardown():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(7)
    yield driver
    driver.quit()

def test_curtir_postagem(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.facebook.com/me/")

    input("Faça login e pressione ENTER para continuar...")

    driver.get("https://www.facebook.com/me/")
    wait = WebDriverWait(driver, 10)

    botoes_curtir = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Curtir"]')
    assert botoes_curtir, "Nenhum botão curtir encontrado."

    botoes_curtir[0].click()

    time.sleep(3)
    print("Teste finalizado: botão Curtir clicado com sucesso.")
