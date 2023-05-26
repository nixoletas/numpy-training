from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('https://sigh.hmilacg.eb.mil.br/paciente')
driver.implicitly_wait(0.5)

username_button = driver.find_element(By.CSS_SELECTOR, "input")
username_button.send_keys("150129")

password_button = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Senha']")
password_button.send_keys('92349')

login_button = driver.find_element(By.NAME, "btn-login")
login_button.click()

print(password_button)

time.sleep(1000)
