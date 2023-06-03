import time
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(5)

    def take_screenshot(self):
        self.browser.find_element(*BasePageLocators.BODY)\
            .screenshot('C://users/Bulatshuh/lazy_load/temp/screenshot.png')

    def scroll_down_pixels(self, pixels):
        self.browser.execute_script(f'window.scrollBy(0, {pixels});')

    def scroll_down_absolute(self):
        height = self.browser.execute_script("return document.body.scrollHeight")
        while int(height) > 1500:
            self.browser.execute_script(f'window.scrollBy(0, 1500);')
            time.sleep(2)
            height -= 1500
        else:
            self.browser.execute_script(f'window.scrollBy(0, 1500);')
            time.sleep(2)

    def go_full_screen(self):
        self.browser.maximize_window()

    def close(self):
        self.browser.quit()
