import time
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage



def test_add_item_to_catalog(browser):
    # link = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    # page = LoginPage(browser, link)
    # page.open_page()
    # page.register_user(email=str(time.time()) + '@list.ru', password=']ncPWkokU2sB7h3')
    link = 'https://selenium1py.pythonanywhere.com/en-gb/'
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_catalogue()
    page.click_add_to_basket_button()
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/'
    page = BasketPage(browser, link)
    page.open_page()
    page.click_view_basket_btn()
    page.should_be_check_button()
    time.sleep(3)