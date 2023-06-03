from pages.base_page import BasePage
from selenium import webdriver
import time


def test_screenshot():
    page = BasePage(webdriver.Chrome(), 'https://stackoverflow.com/questions/20986631/'
                                        'how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python')
    page.open()
    page.go_full_screen()
    page.take_screenshot()
    page.close()
