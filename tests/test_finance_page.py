from locators.finance_page_locators import FinanceLocators
from pages.finace_page import FinancePage
from src.urls import Urls
from src.test_data import TestData

class TestFinance:
    url = Urls()
    test_data = TestData()
    finance_locators = FinanceLocators()

    def test_title(self, driver):
        page = FinancePage(driver,self.url.base_url)
        page.open()
        assert "Google Finance" in page.get_title(), "Google Finance page failed to load"

    def test_compare_stock_symbols(self, driver):
        page = FinancePage(driver, self.url.base_url)
        page.open()
        actual_stock_symbols = page.get_stock_symbols()

        missing_in_ui = [symbol for symbol in self.test_data.test_data if symbol not in actual_stock_symbols]
        extra_in_ui = [symbol for symbol in actual_stock_symbols if symbol not in self.test_data.test_data]

        print(f"Symbols missing in UI: {missing_in_ui}")
        print(f"Extra symbols in UI: {extra_in_ui}")

        assert not missing_in_ui, "Some expected symbols were not found in the UI"
        assert not extra_in_ui, "There were unexpected symbols in the UI"


