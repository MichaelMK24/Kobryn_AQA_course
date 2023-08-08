"""
Write tests for creating a user and logging into the system.
Test to verify the user profile. After that delete all test users from site.
"""
import pytest
import requests
import json


class UserEmailPasswordModel:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


class TestLoginTest:
    def setup_class(self):

        with open(r"C:\Users\misha\PycharmProjects\Kobryn_AQA_course\lesson_18\test_data_test.json") as config:
            lines = json.loads(config.read())
        self.user = UserEmailPasswordModel(lines["test_1_user_email"], lines["test_1_user_password"])
        self.user_2 = UserEmailPasswordModel(lines["test_2_user_email"], lines["test_2_user_password"])

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.session = requests.session()
        yield
        result = self.session.delete(url="https://qauto2.forstudy.space/api/users")
        print(f"User deleted {result}")

    def test_registration_success(self):
        signup_test_data = {
            "name": "Michael",
            "lastName": "Shind",
            "email": self.user.email,
            "password": self.user.password,
            "repeatPassword": self.user.password
        }
        result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=signup_test_data)
        print(f"SignUp request response -> {result.json()}")
        assert result.json()["status"] == "ok"

    def test_get_users_data(self):
        signup_data = {
            "name": "Kobra",
            "lastName": "Nefertari",
            "email": self.user_2.email,
            "password": self.user_2.password,
            "repeatPassword": self.user_2.password
        }
        signup_result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=signup_data)
        print(signup_result.json())

        result = self.session.get(url="https://qauto2.forstudy.space/api/users/profile")
        print(f"Gets authenticated user profile data -> {result.json()}")
        assert result.json()["status"] == "ok"

