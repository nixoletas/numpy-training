from selenium import webdriver
from selenium.webdriver.common.by import By

import time


op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get('https://sigh.hmilacg.eb.mil.br/paciente')
driver.implicitly_wait(0.5)

username_button = driver.find_element(By.CSS_SELECTOR, "input")
print(username_button)
username_button.send_keys("150129")

password_button = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Senha']")
password_button.send_keys('92349')
print(password_button)

login_button = driver.find_element(By.NAME, "btn-login")
login_button.click()

time.sleep(1000)
