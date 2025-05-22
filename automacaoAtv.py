from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/me/")
driver.maximize_window()
driver.implicitly_wait(7)

input("Faça login")

driver.get("https://www.facebook.com/me/")
time.sleep(5)

botoes = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Curtir"]')
if botoes:
    botoes[0].click()

time.sleep(5)
driver.quit()
