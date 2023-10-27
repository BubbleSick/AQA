from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.maximize_window()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # Вычисляем 'y' с использованием функции 'calc'
    y = calc(x)

    element = browser.find_element(By.CSS_SELECTOR, "input#answer")
    element.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # Выбираем радиокнопку
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

