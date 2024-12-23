from selenium.webdriver.common.by import By
from base.basepage import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'https://www.saucedemo.com/inventory.html'

    def check_inventory_page_open(self) -> bool:
        return self.get_current_url() == self.page_url