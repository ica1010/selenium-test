from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurer le WebDriver avec les options et la version spécifiée
driver = webdriver.Chrome()

# Ouvrir la page de connexion Gmail
driver.get("https://pay.kagoservices.com/")

# Attendre que l'élément de l'identifiant soit présent
username = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username.send_keys("misselapp@gmail.com")

password = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password.send_keys("testK@GO228")
try:
    next = driver.find_element(By.ID, 'next_button')
    next.click()
    print('clicked successfuly')
except Exception as e:
    print('error:',e)
user_dropdown_btn = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(By.ID, 'menu_1_66587143347ed_dropdown_1')
)
time.sleep(5)

