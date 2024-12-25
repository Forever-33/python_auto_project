import allure
from selenium.webdriver.common.by import By
from base.basepage import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'https://www.saucedemo.com/inventory.html'
        self.sauce_labs = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.cart_num = (By.CLASS_NAME, 'shopping_cart_badge')
        self.cart_button = (By.ID, 'shopping_cart_container')
        self.sauce_labs_backpack_price = (By.XPATH, '//div[@data-test="inventory-item-price"]')

    @allure.step(r"Проверить, что открыта страница https://www.saucedemo.com/inventory.html")
    def check_inventory_page_open(self) -> bool:
        return self.get_current_url() == self.page_url

    @allure.step(r"Нажать на кнопку добавления товара в корзину")
    def add_to_cart_button_click(self) -> None:
        return self.find_element(*self.sauce_labs).click()

    @allure.step(r"Проверка добавления товара в корзину")
    def get_cart_badge_value(self) -> str:
        return self.find_element(*self.cart_num).text

    @allure.step(r"Нажать на кнопку корзины")
    def cart_button_click(self) -> None:
        return self.find_element(*self.cart_button).click()

    @allure.step(r"Получить цену товара Sauce Labs Backpack на странице с товарами")
    def get_sauce_labs_backpack_price(self) -> str:
        return self.find_element(*self.sauce_labs_backpack_price).text


