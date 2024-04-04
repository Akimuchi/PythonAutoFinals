import time
import selenium.webdriver.common.by
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_page_item_button_is_visible(browser):
    browser.get(link)
    time.sleep(30)
    #проверка страница товара на сайте содержит кнопку добавления в корзину
    assert len(browser.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR, '.btn-add-to-basket')) > 0
