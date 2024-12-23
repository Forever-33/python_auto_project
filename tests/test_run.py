import pytest
from config.base_test import BaseTest


class TestAuth(BaseTest):
    @pytest.mark.parametrize(
        "expected_url, \
        correct_login, \
        correct_password",
        [(
            True,
            'standard_user',
            'secret_sauce'
        )])
    def test_auth(
            self,
            expected_url,
            correct_login,
            correct_password
    ):
        self.auth_page.input_login(correct_login)
        self.auth_page.input_password(correct_password)
        self.auth_page.login_button_click()

        assert self.inventory_page.check_inventory_page_open() == expected_url, \
            "Переход на страницу инвентаря не произошел"

    @pytest.mark.parametrize(
        "expected_url, \
        expected_message, \
        expected_background, \
        correct_login, \
        incorrect_password",
        [(
                True,
                'Epic sadface: Username and password do not match any user in this service',
                'rgba(226, 35, 26, 1)',
                'standard_user',
                'incorrect_password',

        )])
    def test_incorrect_password_auth(
            self,
            expected_url,
            expected_message,
            expected_background,
            correct_login,
            incorrect_password,
    ):
        self.auth_page.input_login(correct_login)
        self.auth_page.input_password(incorrect_password)
        self.auth_page.login_button_click()

        assert self.auth_page.check_login_page() == expected_url, \
            "Переход на страницу инвентаря произошел"
        assert self.auth_page.get_error_message() == expected_message, \
            "Сообщение об ошибке не отображается или не соответствует ожидаемому"
        assert self.auth_page.get_error_background() == expected_background, \
            "Сообщение об ошибке не отображается на красном фоне"

    @pytest.mark.parametrize(
        "expected_url, \
        expected_message, \
        expected_background, \
        correct_login, \
        empty_password",
        [(
                True,
                'Epic sadface: Password is required',
                'rgba(226, 35, 26, 1)',
                'standard_user',
                '',
        )])
    def test_empty_password_auth(
            self,
            expected_url,
            expected_message,
            expected_background,
            correct_login,
            empty_password,
    ):
        self.auth_page.input_login(correct_login)
        self.auth_page.input_password(empty_password)
        self.auth_page.login_button_click()

        assert self.auth_page.check_login_page() == expected_url, \
            "Переход на страницу инвентаря произошел"
        assert self.auth_page.get_error_message() == expected_message, \
            "Сообщение об ошибке не отображается или не соответствует ожидаемому"
        assert self.auth_page.get_error_background() == expected_background, \
            "Сообщение об ошибке не отображается на красном фоне"

    @pytest.mark.parametrize(
        "expected_url, \
        correct_logins, \
        correct_password",
        [
                (True, "standard_user", "secret_sauce"),
                (True, "problem_user", "secret_sauce"),
                (True, "performance_glitch_user", "secret_sauce"),
                (True, "error_user", "secret_sauce"),
                (True, "visual_user", "secret_sauce")
        ])
    def test_empty_password_auth(
            self,
            expected_url,
            correct_logins,
            correct_password,
    ):
        self.auth_page.input_login(correct_logins)
        self.auth_page.input_password(correct_password)
        self.auth_page.login_button_click()

        assert self.inventory_page.check_inventory_page_open() == expected_url, \
            "Переход на страницу инвентаря не произошел"
