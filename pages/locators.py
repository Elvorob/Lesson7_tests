from selenium.webdriver.common.by import By


class MainPageLocators():

    CATALOGUE_LINK = (By.XPATH, "//ul[@id='browse']//ul//a")
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')
    ADD_ITEM_BTN = (By.XPATH, "//div[@class='product_price']//button[@class='btn btn-primary btn-block']")

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')   # CSS_SELECTOR если стоит # это значит что мы ищем по id
    REGISTER_FORM = (By.CSS_SELECTOR,'#login_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR,'#id_registration-password2')
    REG_BTN = (By.XPATH, "//form[@id = 'register_form']//button")

class BasePageLocators():

    USER_ICON = (By.CSS_SELECTOR, '.icon-user') # CSS_SELECTOR если стоит . это значит что мы ищем по class

class BasketPageLocators():

    VIEW_BASKET_BTN = (By.XPATH, '//a[@href="/en-gb/basket/"]')
    CHECKOUT_BTN = (By.XPATH, '//a[@href="/en-gb/checkout/"]')