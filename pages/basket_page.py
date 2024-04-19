from .locators import BasePageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def is_basket_empty_message_present(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_TEXT), \
            "Basket is empty message is not present"

    def is_basket_empty(self):
        assert self.element_is_not_present(*BasePageLocators.BASKET_ITEMS), \
            "Basket have items in it"
