from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose the browser language")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    browser.quit()