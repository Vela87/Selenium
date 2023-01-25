from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
import pytest

from first_page import FirstPage
from second_page import SecondPage
from third_page import ThirdPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
    driver.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in driver.title
    driver.maximize_window()
    yield driver
    driver.quit()


def test_first_page(driver):
    first_page = FirstPage(driver)
    first_page.login()


def test_second_page(driver):
    first_page = FirstPage(driver)
    first_page.login()
    second_page = SecondPage(driver)
    second_page.add_to_cart()


def test_third_page(driver):
    first_page = FirstPage(driver)
    first_page.login()
    second_page = SecondPage(driver)
    second_page.add_to_cart()
    third_page = ThirdPage(driver)
    third_page.checkout()
