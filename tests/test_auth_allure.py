import pytest
import allure
from config.base_test import BaseTest


class TestAuthAllure(BaseTest):
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Авторизация пользователя пустыми значениями")
    @allure.testcase("TMS-001")
    @pytest.mark.parametrize(
        "expected_url, \
        expected_message, \
        expected_background, \
        empty_login, \
        empty_password",
        [(
                True,
                'Epic sadface: Password is required',
                'rgba(226, 35, 26, 1)',
                '',
                '',

        )])
    def test_empty_password_login(
            self,
            expected_url,
            expected_message,
            expected_background,
            empty_login,
            empty_password,
    ):
        self.auth_page.input_login(empty_login)
        assert self.auth_page.get_login_value() == empty_login, \
            "Поле логина не пустое"
        self.auth_page.input_password(empty_password)
        assert self.auth_page.get_password_value() == empty_password, \
            "Поле пароля не пустое"
        self.auth_page.login_button_click()

        assert self.auth_page.check_login_page() == expected_url, \
            "Переход на страницу инвентаря произошел"
        assert self.auth_page.get_error_message() == expected_message, \
            "Сообщение об ошибке не отображается или не соответствует ожидаемому"
        assert self.auth_page.get_error_background() == expected_background, \
            "Сообщение об ошибке не отображается на красном фоне"

