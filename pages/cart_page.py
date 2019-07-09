from .base_page import BasePage

from .locators import BasePageLocators


class CartPage(BasePage):

    def should_be_empty_basket_page(self):
        self.expect_basket_is_empty()
        self.expect_text_that_basket_is_empty()

    def expect_basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BUTTON_PROCEED_TO_CHECKOUT), "Basket  is not empty"

    def expect_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET), "Basket  is not empty"
