"""
Write tests for creating a user and logging into the system.
Test to verify the user profile. After that delete all test users from site.
"""
import requests
import json


class UserLoginModel:
    def __init__(self, email: str, password: str, remember: bool):
        self.email = email
        self.password = password
        self.remember = remember


class UserEmailPasswordModel:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


class TestLoginTest:
    def setup_class(self):

        with open("test_data.json") as config:
            lines = json.loads(config.read())
        self.user = UserEmailPasswordModel(lines["test_1_user_email"], lines["test_1_user_password"])
        self.session = requests.session()

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
        result = self.session.get(url="https://qauto2.forstudy.space/api/users/profile")
        print(f"Gets authenticated user profile data -> {result.json()}")
        assert result.json()["status"] == "ok"

    def teardown_class(self):
        user_login = UserLoginModel(self.user.email, self.user.password, False)
        self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_login.__dict__)

        result = self.session.delete(url="https://qauto2.forstudy.space/api/users")
        print(result)
