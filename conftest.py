import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.set_preference("dom.disable_beforeunload", True)
    options.page_load_strategy = 'eager'
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()
