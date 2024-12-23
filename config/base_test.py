import pytest
from base.pages.inventory_page import InventoryPage
from base.pages.login_page import LoginPage


class BaseTest:
    driver: None
    auth_page: LoginPage
    inventory_page: InventoryPage

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.auth_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
