import allure
from selenium.webdriver.common.by import By
from base.basepage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'https://www.saucedemo.com/cart.html'
        self.cart_item_container = (By.CLASS_NAME, 'cart_item')
        self.cart_item_one = (By.CLASS_NAME, 'cart_quantity')
        self.cart_item_name = (By.CSS_SELECTOR, '#item_4_title_link')
        self.cart_item_price = (By.XPATH, '//div[@class="inventory_item_price"]')
        self.checkout_button = (By.ID, 'checkout')

    @allure.step(r"Проверить, что открыта страница https://www.saucedemo.com/cart.html")
    def check_cart_page_open(self) -> bool:
        return self.get_current_url() == self.page_url

    @allure.step(r"Проверить количество товаров в корзине")
    def check_cart_item_count(self) -> int:
        return len(self.find_elements(*self.cart_item_container))

    @allure.step(r"Проверить что товара 1 единица")
    def check_cart_item_one(self) -> int:
        return len(self.find_elements(*self.cart_item_one))

    @allure.step(r"Проверить, что товар Sauce Labs Backpack")
    def check_item_sauce_labs_backpack(self) -> str:
        return self.find_element(*self.cart_item_name).text

    @allure.step(r"Получить цену товара в корзине и сравнить с ценой на странице товаров")
    def get_cart_item_price(self) -> str:
        return self.find_element(*self.cart_item_price).text

    @allure.step(r"Нажать на кнопку Checkout")
    def checkout_button_click(self) -> None:
        self.find_element(*self.checkout_button).click()
