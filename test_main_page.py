import time
from .pages.main_page import MainPage
import pytest
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

link = "https://selenium1py.pythonanywhere.com/ru/"


# class TestMainPage():

# def setup(self):  # Перенесено в текстуру
#     self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# маркеры указываются в файлк pytest.ini и позволяют группировать тесты по маркеру запускать их поочереди если у них стоит маркер
# например: в строке терминала мы пишем pytest -s -v -m "open_page" test_main_page.py
# и запустятся все тесты с маркером @pytest.mark.open_page
@pytest.mark.open_page
# @pytest.mark.smoke
def test_guest_can_go_to_catalogue(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_view_products()
    page.go_to_catalogue()


# @pytest.mark.view_products
# @pytest.mark.xfail
# def test_2(self, browser):
#         browser.get(link)
#         # browser.find_element(By.XPATH, "//ul[@id='browse']//ul//a").click() # убрали эту строчку в файл main_page.py
#         # browser.find_element(By.XPATH, "//ul[@id='browse']//ul//").click() # строчка для илюстрации маркера xfail
#     time.sleep(1)

# def teardown(self):  # Перенесено в текстуру
#     self.driver.quit()
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_logi_page()
    page = LoginPage(browser, link)
    page.should_be_login_page()


def test_user_should_be_autorized(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.register_user(email=str(time.time()) + "@list.ru", password="]ncPWkokU2sB7h3")
    page.should_be_autorized_user()


@pytest.mark.smoke
def add_item_to_catalog(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.register_user(email=str(time.time()) + "@list.ru", password="]ncPWkokU2sB7h3")
    # page.should_be_autorized_user()
    # link = 'https://selenium1py.pythonanywhere.com/en-gb/'
    # page = MainPage(browser, link)
    # page.open_page()
    # page.go_to_catalogue()
    # page.click_add_to_basket_button()
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    page = BasketPage(browser, link)
    page.open_page()
    page.click_view_basket_btn()
    time.sleep(3)
