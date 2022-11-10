import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser...")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print("\nQuit browser")
    browser.quit()
