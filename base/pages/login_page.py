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

    def input_login(self, login: str) -> None:
        self.find_element(*self.login).send_keys(login)

    def input_password(self, password: str) -> None:
        self.find_element(*self.password).send_keys(password)

    def login_button_click(self) -> None:
        self.find_element(*self.login_btn).click()

    def check_login_page(self) -> bool:
        return self.get_current_url() == self.page_url

    def get_error_message(self) -> str:
        return self.find_element(*self.password_error).text

    def get_error_background(self) -> str:
        return self.find_element(*self.background_error).value_of_css_property('background-color')
