class Selenium_Helper:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)


