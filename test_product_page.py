from .pages.product_page import ProductPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.item_name_in_cart_is_correct()
    page.item_price_in_cart_is_correct()
