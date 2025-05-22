from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
#from dotenv import load_dotenv
#import os
import time

# Carregar variáveis do arquivo .env
#load_dotenv()

# Obter email e senha do .env
#FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
#FACEBOOK_SENHA = os.getenv("FACEBOOK_SENHA")

# Inicializar o driver do navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessar o site
driver.get("https://www.facebook.com/me/")
driver.maximize_window()
driver.implicitly_wait(10)

input("Faça login manualmente")

driver.get("https://www.facebook.com/me/")
# # Função de login
# def login(driver, email, senha):
#     campo_email = driver.find_element(By.ID, "email")
#     campo_email.send_keys(email)

#     campo_senha = driver.find_element(By.ID, "pass")
#     campo_senha.send_keys(senha)

#     btn_login = driver.find_element(By.NAME, "login")
#     btn_login.click()

#     time.sleep(5)

# Executar o login com as variáveis carregadas do .env
#login(driver, FACEBOOK_EMAIL, FACEBOOK_SENHA)

# Espera para visualizar o resultado (opcional)
time.sleep(5)
driver.quit()



