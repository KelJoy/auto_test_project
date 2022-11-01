from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
from .pages.basket_page import BasketPage
from selenium.common.exceptions import NoAlertPresentException


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.go_to_basket()
	basket_page= BasketPage(browser,browser.current_url)
	basket_page.basket_should_be_empty()
	basket_page.should_be_message_about_empty_basket()