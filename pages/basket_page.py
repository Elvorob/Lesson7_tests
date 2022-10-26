from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def click_view_basket_btn(self):
        self.browser.find_element(*BasketPageLocators.VIEW_BASKET_BTN).click()
