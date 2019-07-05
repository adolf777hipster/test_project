import re

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.message_add_to_basket_present()
        self.comparison_book_name()
        self.comparison_price()

    def add_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def should_be_product_page_url(self):
        pattern = re.compile(
            r'http://selenium1py\.pythonanywhere\.com/.*/catalogue/the-shellcoders-handbook_209/\?promo=newYear')
        assert pattern.match(self.browser.current_url), "Incorrect URL"

    def message_add_to_basket_present(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ADD_TO_BASKET), "Add message is not presented"

    def comparison_book_name(self):
        book_name_in_message = self.browser.find_element(*BasketPageLocators.MESSAGE_ADD_TO_BASKET).text
        book_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME).text
        assert book_name == book_name_in_message, \
            "The name of product in the message doesn't coincide with the product that you really added"

    def comparison_price(self):
        product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        product_price_in_basket = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, \
            "Basket total is not equals product price"
