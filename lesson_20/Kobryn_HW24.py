"""
Add classes for driver, pages, and UI elements (button, textbox, etc...) for previous homework
"""
import requests

from Kobryn_AQA_course.lesson_20.constants.api_url_constants import POST_USER_SIGNUP
from Kobryn_AQA_course.lesson_20.constants.url_constants import DEFAULT_API_URL
from Kobryn_AQA_course.lesson_20.constants.user_credentials import (
    USER_BASE_EMAIL,
    USER_BASE_PASSWORD,
    TEST_USER_CORRECT_NAME,
    TEST_USER_CORRECT_LASTNAME,
)


class UserCreatedByApi:
    def __init__(self):
        self.session = requests.session()

    def create_user_by_api(self):
        signup_test_data = {
            "name": TEST_USER_CORRECT_NAME,
            "lastName": TEST_USER_CORRECT_LASTNAME,
            "email": USER_BASE_EMAIL,
            "password": USER_BASE_PASSWORD,
            "repeatPassword": USER_BASE_PASSWORD,
        }
        result = self.session.post(
            url=f"{DEFAULT_API_URL}{POST_USER_SIGNUP}", json=signup_test_data
        )
        print(f"SignUp request response -> {result.json()}")
