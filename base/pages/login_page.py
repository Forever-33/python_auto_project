import allure
from selenium.webdriver.common.by import By
from base.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.login = (By.ID, 'user-name')           #Локатор по ID для элемента строки ввода login
        self.password = (By.ID, 'password')         #Локатор по ID для элемента строки ввода password
        self.password_error = (By.CLASS_NAME, 'error-message-container')
        self.background_error = (By.CSS_SELECTOR, '.error-message-container.error')
        self.login_btn = (By.NAME, 'login-button')  #Локатор по Name для элемента кнопка Login
        self.page_url = 'https://www.saucedemo.com/'

    @allure.step(r"Найти элемент текстового поля для логина")
    def input_login(self, login: str) -> None:
        self.find_element(*self.login).send_keys(login)

    @allure.step(r"Найти элемент текстового поля для пароля")
    def input_password(self, password: str) -> None:
        self.find_element(*self.password).send_keys(password)

    @allure.step(r"Нажать на кнопку авторизации")
    def login_button_click(self) -> None:
        self.find_element(*self.login_btn).click()

    @allure.step(r"Проверить, что открыта страница https://www.saucedemo.com")
    def check_login_page(self) -> bool:
        return self.get_current_url() == self.page_url

    @allure.step(r"Найти элемент всплывающей ошибки при авторизации")
    def get_error_message(self) -> str:
        return self.find_element(*self.password_error).text

    @allure.step(r"Проверить, что цвет заднего фона ошибки соответствует заданному")
    def get_error_background(self) -> str:
        return self.find_element(*self.background_error).value_of_css_property('background-color')

    @allure.step(r"Проверить текстовое поле логина на значение")
    def get_login_value(self) -> str:
        return self.find_element(*self.login).get_attribute('value')

    @allure.step(r"Проверить текстовое поле пароля на значение")
    def get_password_value(self) -> str:
        return self.find_element(*self.password).get_attribute('value')
