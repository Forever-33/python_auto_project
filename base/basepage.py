<<<<<<< zadacha_1
=======
from selenium.common import TimeoutException
>>>>>>> main
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
<<<<<<< zadacha_1
=======
from selenium.webdriver.support import expected_conditions as ec
>>>>>>> main


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = ''

    def find_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By or int, value: str) -> [WebElement]:
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    def get_current_url(self) -> str:
        return self.driver.current_url
<<<<<<< zadacha_1
=======

    def is_element_present(self, by, value):
        try:
            WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False
>>>>>>> main
