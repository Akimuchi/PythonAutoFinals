from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear]"])
def test_guest_can_add_product_to_basket(browser, link):
    page_link = link
    page = ProductPage(browser, page_link)
    page.open()
    page.should_be_product_page()
    time.sleep(10)
    page.add_to_cart()
    time.sleep(10)
    page.solve_quiz_and_get_code()
    page.item_name_in_cart_is_correct()
    page.item_price_in_cart_is_correct()
