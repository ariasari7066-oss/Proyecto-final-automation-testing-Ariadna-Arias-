from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- DRIVER CONFIG ---
def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

# --- CONSTANTES ---
URL = 'https://www.saucedemo.com/'
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

NOMBRE = "Ariadna"
APELLIDO = "Arias"
CODIGO_POSTAL = "1058"