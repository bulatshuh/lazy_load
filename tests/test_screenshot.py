from pages.base_page import BasePage
from selenium import webdriver
import time


def test_screenshot():
    page = BasePage(webdriver.Chrome(), 'https://www.yahoo.com')
    page.open()
    page.go_full_screen()
    page.scroll_down_absolute()
    page.take_screenshot()
    time.sleep(3)
    page.close()
