from .base_page import BasePage

# from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_view_products(self):
        assert self.element_is_present(*MainPageLocators.CATALOGUE_LINK)

    def go_to_catalogue(self):
        self.browser.find_element(*MainPageLocators.CATALOGUE_LINK).click()

    def go_to_logi_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()

    def click_add_to_basket_button(self):
        self.browser.find_element(*MainPageLocators.ADD_ITEM_BTN).click()
