import pytest
<<<<<<< zadacha_1
=======

from base.pages.cart_page import CartPage
from base.pages.checkout_complete_page import CheckoutCompletePage
from base.pages.checkout_page_step_one import CheckoutPageStepOne
from base.pages.checkout_page_step_two import CheckoutPageStepTwo
>>>>>>> main
from base.pages.inventory_page import InventoryPage
from base.pages.login_page import LoginPage


class BaseTest:
    driver: None
    auth_page: LoginPage
    inventory_page: InventoryPage
<<<<<<< zadacha_1
=======
    cart_page: CartPage
    checkout_page_step_one: CheckoutPageStepOne
    checkout_page_step_two: CheckoutPageStepTwo
    checkout_complete_page: CheckoutCompletePage
>>>>>>> main

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.auth_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
<<<<<<< zadacha_1
=======
        self.cart_page = CartPage(driver)
        self.checkout_page_step_one = CheckoutPageStepOne(driver)
        self.checkout_page_step_two = CheckoutPageStepTwo(driver)
        self.checkout_complete_page = CheckoutCompletePage(driver)
>>>>>>> main
