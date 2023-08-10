"""
Create an autotest to check the functionality of adding a car to a user's garage:
steps:
Create User by API - done
Login to https://qauto2.forstudy.space/ using selenium - done
Add a car using selenium - done
Check car in garage using selenium AND API - done
In teardown remove all data, created in the test - done
"""
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserCreatedByApi:
    def __init__(self):
        self.email = "testuserforcar3@car.com"
        self.password = "Qwerty3562car1"
        self.session = requests.session()

    def create_user_by_api(self):
        signup_test_data = {
            "name": "Michael",
            "lastName": "Kobryn",
            "email": self.email,
            "password": self.password,
            "repeatPassword": self.password,
        }
        result = self.session.post(
            url="https://qauto2.forstudy.space/api/auth/signup", json=signup_test_data
        )
        print(f"SignUp request response -> {result.json()}")

    # def user_by_api_logout(self):
    #     logout_result = self.session.get(url="https://qauto2.forstudy.space/api/auth/logout")
    #     print(logout_result.json())


class AddCarToGarage:
    def __init__(self):
        self.user = UserCreatedByApi()
        self.Url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
        self.driver = webdriver.Chrome()

    def login_with_selenium(self):
        self.driver.get(self.Url)
        sign_in_button = self.driver.find_element(
            By.XPATH, "//div//button[text()='Sign In']"
        )
        sign_in_button.click()

        email_field = self.driver.find_element(By.ID, "signinEmail")
        email_field.send_keys(self.user.email)

        password_field = self.driver.find_element(By.ID, "signinPassword")
        password_field.send_keys(self.user.password)

        login_button = self.driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

    def add_car_with_selenium(self):
        add_car_button = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Add car']"))
        )
        add_car_button.click()

        brand_select_dropdown = self.driver.find_element(By.ID, "addCarBrand")
        brand_select_dropdown.click()

        brand_select = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//option[text()='Porsche']"))
        )
        brand_select.click()

        model_select_dropdown = self.driver.find_element(By.ID, "addCarModel")
        model_select_dropdown.click()

        # get element after explicitly waiting for 1 seconds
        model_select = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//option[text()='Cayenne']"))
        )
        model_select.click()

        mileage_field = self.driver.find_element(By.ID, "addCarMileage")
        mileage_field.send_keys("52000")

        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add']")
        add_button.click()
