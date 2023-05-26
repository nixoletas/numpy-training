import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

import requests

login_url = "https://sigh.hmilacg.eb.mil.br/paciente/login.php"
username = "150129"
password = "92349"

# create a requests session to persist cookies across requests
with requests.Session() as session:
    # send a GET request to the login page to retrieve the initial cookies
    response = session.get(login_url)
    
    # extract the CSRF token from the response cookies
    csrf_token = response.cookies["csrf_token"]
    
    # construct the data payload for the login request
    data = {
        "csrf_token": csrf_token,
        "login": username,
        "senha": password,
        "acessar": "Entrar",
    }
    
    # send a POST request to the login endpoint with the data payload
    response = session.post(login_url, data=data)
    
    # check if the login was successful by inspecting the response HTML
    if "Bem-vindo" in response.text:
        print("Login successful!")
    else:
        print("Login failed.")
