import pytest
import allure
from config.base_test import BaseTest


class TestSauceLabs(BaseTest):
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Авторизация пользователя c корректным логином и паролем")
    @allure.testcase("TMS-002")
    @pytest.mark.parametrize(
        "expected_url, \
        correct_login, \
        correct_password, \
        cart_badge_value, \
        cart_item_count, \
        item_name, \
        first_name, \
        last_name, \
        postal_code, \
        payment_info_label, \
        payment_info_value, \
        shipping_info_label, \
        shipping_info_value, \
        total_info_label, \
        subtotal_label, \
        tax_label, \
        total_label, \
        checkout_complete_title, \
        complete_header, \
        complete_text",
        [(
                True,
                'standard_user',
                'secret_sauce',
                '1',
                1,
                'Sauce Labs Backpack',
                'Joe',
                'Lowson',
                '1234',
                'Payment Information:',
                'SauceCard #31337',
                'Shipping Information:',
                'Free Pony Express Delivery!',
                'Price Total',
                'Item total: $29.99',
                'Tax: $2.40',
                'Total: $32.39',
                'Checkout: Complete!',
                'Thank you for your order!',
                'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        )])
    def test_correct_login_password(
            self,
            expected_url,
            correct_login,
            correct_password,
            cart_badge_value,
            cart_item_count,
            item_name,
            first_name,
            last_name,
            postal_code,
            payment_info_label,
            payment_info_value,
            shipping_info_label,
            shipping_info_value,
            total_info_label,
            subtotal_label,
            tax_label,
            total_label,
            checkout_complete_title,
            complete_header,
            complete_text
    ):
        self.auth_page.input_login(correct_login)
        self.auth_page.input_password(correct_password)
        self.auth_page.login_button_click()
        assert self.inventory_page.check_inventory_page_open() == expected_url, \
            "Переход на страницу инвентаря не произошел"

        inventory_price = self.inventory_page.get_sauce_labs_backpack_price()

        self.inventory_page.add_to_cart_button_click()
        assert self.inventory_page.get_cart_badge_value() == cart_badge_value, \
            "Товар не добавлен в корзину"

        self.inventory_page.cart_button_click()
        assert self.cart_page.check_cart_page_open() == expected_url, \
            "Переход на страницу инвентаря не произошел"
        assert self.cart_page.check_cart_item_count() == cart_item_count, \
            "Количество товаров в корзине не равно 1"
        assert self.cart_page.check_item_sauce_labs_backpack() == item_name, \
            "Товар не имеет имя Sauce Labs Backpack"

        cart_price = self.cart_page.get_cart_item_price()
        assert cart_price == inventory_price, \
            f"Цена товара в корзине ({cart_price}) не совпадает с ценой \
            на странице со списком товаров ({inventory_price})"

        self.cart_page.checkout_button_click()

        self.checkout_page_step_one.input_first_name(first_name)
        self.checkout_page_step_one.input_last_name(last_name)
        self.checkout_page_step_one.input_postal_code(postal_code)
        self.checkout_page_step_one.continue_button_click()

        assert self.checkout_page_step_two.check_checkout_item_one() == cart_item_count, \
            "Количество товаров в Checkout не равно 1"
        assert self.checkout_page_step_two.check_checkout_sauce_labs_backpack() == item_name, \
            "Товар не имеет имя Sauce Labs Backpack"

        checkout_price = self.checkout_page_step_two.get_checkout_item_price()
        assert checkout_price == inventory_price, \
            f"Цена товара в корзине ({checkout_price}) не совпадает с ценой \
            на странице со списком товаров ({inventory_price})"

        assert self.checkout_page_step_two.check_payment_info_label() == payment_info_label, \
            f"Заголовок Payment Information: не найден или не соответствует \
            ожидаемому значению ({payment_info_label})"

        assert self.checkout_page_step_two.check_payment_info_value() == payment_info_value, \
            f"Значение SauceCard #31337 не найдено или не соответствует \
            ожидаемому значению ({payment_info_value})"

        assert self.checkout_page_step_two.check_shipping_info_label() == shipping_info_label, \
            f"Заголовок Shipping Information: не найден или не соответствует \
            ожидаемому значению ({shipping_info_label})"

        assert self.checkout_page_step_two.check_shipping_info_value() == shipping_info_value, \
            f"Значение Free Pony Express Delivery! не найдено или не соответствует \
            ожидаемому значению ({shipping_info_value})"

        assert self.checkout_page_step_two.check_total_info_label() == total_info_label, \
            f"Заголовок Price Total: не найден или не соответствует ожидаемому значению ({total_info_label})"

        assert self.checkout_page_step_two.check_subtotal_label() == subtotal_label, \
            f"Значение Item total: не найдено или не соответствует ожидаемому значению ({subtotal_label})"

        assert self.checkout_page_step_two.check_tax_label() == tax_label, \
            f"Значение Tax: не найдено или не соответствует ожидаемому значению ({tax_label})"

        subtotal_value = self.checkout_page_step_two.get_subtotal_value()
        tax_value = self.checkout_page_step_two.get_tax_value()
        total_value = self.checkout_page_step_two.get_total_value()
        expected_total = subtotal_value + tax_value
        assert total_value == expected_total, \
            f"Значение Total: ({total_value}) не соответствует сумме \
            Item total ({subtotal_value}) и Tax ({tax_value})"

        self.checkout_page_step_two.finish_button_click()

        assert self.checkout_complete_page.check_checkout_complete_page_open() == expected_url, \
            "Переход на страницу Checkout: Complete! не произошел"

        assert self.checkout_complete_page.check_checkout_complete_title() == checkout_complete_title, \
            f"Поле Checkout: Complete! не найдено или не соответствует \
            ожидаемому значению ({checkout_complete_title})"

        assert self.checkout_complete_page.check_complete_header() == complete_header, \
            f"Заголовок Thank you for your order! не найден или не \
            соответствует ожидаемому значению ({complete_header})"

        assert self.checkout_complete_page.check_complete_text() == complete_text, \
            f"Заголовок Your order has been dispatched, and will arrive just as fast as the pony can get there! не найден или не соответствует ожидаемому значению ({complete_text})"

        assert self.checkout_complete_page.check_back_home_button(), \
            "Кнопка Back Home не найдена"
