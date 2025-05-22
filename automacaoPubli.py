from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com/me/")
driver.implicitly_wait(7)

input("Faça login")


area_de_publicar = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"No que você está pensando")]'))
)
area_de_publicar.click()


caixa_texto = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[contenteditable="true"]'))
)

texto_para_postar = "post automatizado"

caixa_texto.clear()
caixa_texto.send_keys(texto_para_postar)


botao_postar = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="Postar"]'))
)
botao_postar.click()

time.sleep(5)
driver.quit()
