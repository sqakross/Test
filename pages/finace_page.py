from pages.base_page import BasePage
from locators.finance_page_locators import FinanceLocators
from src.urls import Urls

class FinancePage(BasePage):
    locators = FinanceLocators()

    def get_title(self):
        self.title_contains("Google Finance")
        return self.driver.title

    def get_stock_symbols(self):
        # Assuming there's a section with the following ID/class or a similar locator
        stock_elements = self.elements_all_presence(self.locators.STOCK_NAME)
        return  [stock.text for stock in stock_elements]




