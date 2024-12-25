import allure
from selenium.webdriver.common.by import By
from base.basepage import BasePage


class CheckoutPageStepOne(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/checkout-step-one.html'
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.postal_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')

    @allure.step(r"Проверить, что открыта страница https://www.saucedemo.com/checkout-step-one.html")
    def check_checkout_step_one_page_open(self) -> bool:
        return self.get_current_url() == self.page_url

    @allure.step(r"Заполнить поле First Name")
    def input_first_name(self, first_name: str) -> None:
        self.find_element(*self.first_name_input).send_keys(first_name)

    @allure.step(r"Заполнить поле Last Name")
    def input_last_name(self, last_name: str) -> None:
        self.find_element(*self.last_name_input).send_keys(last_name)

    @allure.step(r"Заполнить поле Zip/Postal Code")
    def input_postal_code(self, postal_code: str) -> None:
        self.find_element(*self.postal_code_input).send_keys(postal_code)

    @allure.step(r"Нажать на кнопку Continue")
    def continue_button_click(self) -> None:
        self.find_element(*self.continue_button).click()
