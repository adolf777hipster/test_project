import re

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.should_not_be_success_message()
        self.message_add_to_basket_present()
        self.comparison_book_name()
        self.comparison_price()

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def should_be_product_page_url(self):
        pattern = re.compile(
            r'http://selenium1py\.pythonanywhere\.com/.*/catalogue/.*/\?promo=.*')
        assert pattern.match(self.browser.current_url), "Incorrect URL"

    def message_add_to_basket_present(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Add message is not presented"

    def comparison_book_name(self):
        book_name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == book_name_in_message, \
            "The name of product in the message doesn't coincide with the product that you really added"

    def comparison_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, \
            "Basket total is not equals product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"