import allure
from selenium.webdriver.common.by import By
from base.basepage import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/checkout-complete.html'
        self.secondary_header = (By.CSS_SELECTOR, '[data-test="secondary-header"]')
        self.title = (By.CSS_SELECTOR, '[data-test="title"]')
        self.complete_header = (By.CSS_SELECTOR, '[data-test="complete-header"]')
        self.complete_text = (By.CSS_SELECTOR, '[data-test="complete-text"]')
        self.back_home_button = (By.ID, 'back-to-products')

    @allure.step(r"Проверить, что открыта страница https://www.saucedemo.com/checkout-complete.html")
    def check_checkout_complete_page_open(self) -> bool:
        return self.get_current_url() == self.page_url

    @allure.step(r"Проверить, что присутствует поле Checkout: Complete!")
    def check_checkout_complete_title(self) -> str:
        return self.find_element(*self.title).text

    @allure.step(r"Проверить, что присутствует заголовок Thank you for your order!")
    def check_complete_header(self) -> str:
        return self.find_element(*self.complete_header).text

    @allure.step(r"Проверить, что присутствует заголовок Your order has been dispatched, and will arrive just as fast as the pony can get there!")
    def check_complete_text(self) -> str:
        return self.find_element(*self.complete_text).text

    @allure.step(r"Проверить, что присутствует кнопка Back Home")
    def check_back_home_button(self) -> bool:
        return self.is_element_present(*self.back_home_button)


