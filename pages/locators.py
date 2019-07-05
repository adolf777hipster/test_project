from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_REGISTER = (By.ID, "register_form")


class BasketPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner>:nth-child(1)>strong")
    MESSAGE_ADD_TO_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div h1")
