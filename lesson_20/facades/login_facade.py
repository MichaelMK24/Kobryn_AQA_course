import allure

from ..constants.user_credentials import (
    USER_BASE_EMAIL,
    USER_BASE_PASSWORD,
)
from .base_facade import BaseFacade


class LoginFacade(BaseFacade):
    def __init__(self):
        super().__init__()

    def fill_all_fields_on_login_form(
        self, email=USER_BASE_EMAIL, password=USER_BASE_PASSWORD, is_click=True
    ):
        self.fill_email_field_on_login_form(email)

        self.fill_password_field_on_login_form(password)

        if is_click:
            self.click_login_button_on_login_form()

    @allure.step("Login full cycle")
    def login_full_cycle(self, email=USER_BASE_EMAIL, password=USER_BASE_PASSWORD):
        self.click_sign_in_from_default_page()
        self.fill_all_fields_on_login_form(email, password)

    @allure.step("set_email_field")
    def fill_email_field_on_login_form(self, email):
        self.login_page.email_field().send_keys(email)

    @allure.step("set_password_field")
    def fill_password_field_on_login_form(self, password):
        self.login_page.password_field().send_keys(password)

    def click_login_button_on_login_form(self):
        self.login_page.login_button().click()

    def click_sign_in_from_default_page(self):
        self.navigation_bar_page.sign_in_button().click()
