import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")

@pytest.fixture(scope="session")
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
