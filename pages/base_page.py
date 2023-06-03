class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(5)

    def take_screenshot(self):
        self.browser.get_screenshot_as_file('/tmp/google.png')

    def scroll_down_pixels(self, pixels):
        self.browser.execute_script(f'window.scrollBy(0, {pixels});')

    def close(self):
        self.browser.quit()
