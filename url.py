from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    print(text_box)
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    print(submit_button)

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    print(message)
    value = message.text
    assert value == "Received!"
    time.sleep(1000)

test_eight_components()