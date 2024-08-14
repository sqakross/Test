from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    timeout = 10

    # locators = LoginLocators()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def elements_all_presence(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def title_contains(self, text, timeout=timeout):
        return wait(self.driver, timeout).until(EC.title_contains(text))
