from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..ui_elements.button import Button


class NavigationBarPage(BasePage):
    def __init__(self):
        super().__init__()
        self.sign_in_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//div//button[text()='Sign In']")
        )
