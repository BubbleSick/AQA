from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


try:
    # Инициализация драйвера Chrome
    browser = webdriver.Chrome()

    # Открыть страницу
    browser.get("https://suninjuly.github.io/selects1.html")

    # Найти элементы с числами и сложить их значения
    element1 = browser.find_element(By.ID, "num1")
    element2 = browser.find_element(By.ID, "num2")

    num1 = int(element1.text)
    num2 = int(element2.text)

    # Выбрать значение в выпадающем списке, равное сумме чисел
    total = num1 + num2
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(total))



    # Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Пауза перед закрытием браузера
    time.sleep(10)
    browser.quit()