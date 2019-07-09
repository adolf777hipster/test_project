from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import re


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        pattern = re.compile(r'http://selenium1py\.pythonanywhere\.com/.*/accounts/login/')
        assert pattern.match(self.browser.current_url)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "Register form is not presented"

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*BasePageLocators.EMAIL_ADDRESS)
        email_address.send_keys(email)
        password_link = self.browser.find_element(*BasePageLocators.PASSWORD)
        password_link.send_keys(password)
        confirm_password_link = self.browser.find_element(*BasePageLocators.CONFIRM_PASSWORD)
        confirm_password_link.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register.click()
