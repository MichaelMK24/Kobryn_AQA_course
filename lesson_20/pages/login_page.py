from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..ui_elements.text_box import TextBox
from ..ui_elements.button import Button


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

        self.email_field = lambda: TextBox(
            self._driver.find_element(By.ID, "signinEmail")
        )

        self.password_field = lambda: TextBox(
            self._driver.find_element(By.ID, "signinPassword")
        )

        self.login_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Login']")
        )
