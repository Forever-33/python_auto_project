import allure
from selenium.webdriver.common.by import By
from base.basepage import BasePage


class CheckoutPageStepTwo(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/checkout-step-two.html'
        self.checkout_item_one = (By.CLASS_NAME, 'cart_quantity')
        self.checkout_item_name = (By.CSS_SELECTOR, '#item_4_title_link')
        self.checkout_item_price = (By.XPATH, '//div[@class="inventory_item_price"]')
        self.payment_info_label = (By.CSS_SELECTOR, '[data-test="payment-info-label"]')
        self.payment_info_value = (By.CSS_SELECTOR, '[data-test="payment-info-value"]')
        self.shipping_info_label = (By.CSS_SELECTOR, '[data-test="shipping-info-label"]')
        self.shipping_info_value = (By.CSS_SELECTOR, '[data-test="shipping-info-value"]')
        self.total_info_label = (By.CSS_SELECTOR, '[data-test="total-info-label"]')
        self.subtotal_label = (By.CSS_SELECTOR, '[data-test="subtotal-label"]')
        self.tax_label = (By.CSS_SELECTOR, '[data-test="tax-label"]')
        self.total_label = (By.CSS_SELECTOR, '[data-test="total-label"]')
        self.finish_button = (By.ID, 'finish')

    @allure.step(r"Проверить, что открыта страница https://www.saucedemo.com/checkout-step-two.html")
    def check_checkout_step_two_page_open(self) -> bool:
        return self.get_current_url() == self.page_url

    @allure.step(r"Проверить что товара 1 единица")
    def check_checkout_item_one(self) -> int:
        return len(self.find_elements(*self.checkout_item_one))

    @allure.step(r"Проверить, что товар Sauce Labs Backpack")
    def check_checkout_sauce_labs_backpack(self) -> str:
        return self.find_element(*self.checkout_item_name).text

    @allure.step(r"Получить цену товара в Checkout и сравнить с ценой на странице товаров")
    def get_checkout_item_price(self) -> str:
        return self.find_element(*self.checkout_item_price).text

    @allure.step(r"Проверить, что присутствует заголовок Payment Information:")
    def check_payment_info_label(self) -> str:
        return self.find_element(*self.payment_info_label).text

    @allure.step(r"Проверить, что значение SauceCard #31337")
    def check_payment_info_value(self) -> str:
        return self.find_element(*self.payment_info_value).text

    @allure.step(r"Проверить, что присутствует заголовок Shipping Information:")
    def check_shipping_info_label(self) -> str:
        return self.find_element(*self.shipping_info_label).text

    @allure.step(r"Проверить, что значение Free Pony Express Delivery!")
    def check_shipping_info_value(self) -> str:
        return self.find_element(*self.shipping_info_value).text

    @allure.step(r"Проверить, что присутствует заголовок Price Total")
    def check_total_info_label(self) -> str:
        return self.find_element(*self.total_info_label).text

    @allure.step(r"Проверить, что значение Item total: совпадает с указанной на странице со списком товаров")
    def check_subtotal_label(self) -> str:
        return self.find_element(*self.subtotal_label).text

    @allure.step(r"Проверить, что значение Tax: имеет значение 2.40")
    def check_tax_label(self) -> str:
        return self.find_element(*self.tax_label).text

    @allure.step(r"Получить значение Item total")
    def get_subtotal_value(self) -> float:
        subtotal_text = self.find_element(*self.subtotal_label).text
        return float(subtotal_text.replace('Item total: $', ''))

    @allure.step(r"Получить значение Tax")
    def get_tax_value(self) -> float:
        tax_text = self.find_element(*self.tax_label).text
        return float(tax_text.replace('Tax: $', ''))

    @allure.step(r"Получить значение Total")
    def get_total_value(self) -> float:
        total_text = self.find_element(*self.total_label).text
        return float(total_text.replace('Total: $', ''))

    @allure.step(r"Нажать кнопку Finish")
    def finish_button_click(self):
        self.find_element(*self.finish_button).click()

