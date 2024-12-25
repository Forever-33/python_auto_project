import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--enable-javascript')
    _driver = webdriver.Chrome(options=options)
    _driver.get('https://www.saucedemo.com')
    yield _driver
    _driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.instance.driver
        if driver:
            allure.attach(
                name='Скриншот',
                body=driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
        else:
            print(f"Driver not found in test {node.name}")
