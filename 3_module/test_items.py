import time
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert add_to_basket_button is not None