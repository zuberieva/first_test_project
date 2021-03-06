from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('link',
                         ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                          pytest.param(
                              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                              marks=pytest.mark.xfail),
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(link, browser):
    page = ProductPage(browser, link)
    page.open()
    page.action_on_product_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())

        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link1 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        page = ProductPage(browser, link1)
        page.open()
        page.action_on_product_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button_add_to_basket()
    page.should_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
