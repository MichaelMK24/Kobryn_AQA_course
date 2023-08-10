from Kobryn_HW22 import AddCarToGarage, UserCreatedByApi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddCarTest:
    def setup_class(self):
        self.add_car1 = AddCarToGarage()
        self.user_car = UserCreatedByApi()
        self.user_car.create_user_by_api()

    def test_check_car_selenium_test(self):
        self.add_car1.login_with_selenium()
        self.add_car1.add_car_with_selenium()
        result = WebDriverWait(self.add_car1.driver, 2).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//p[text()='Porsche Cayenne']"), "Porsche Cayenne"
            )
        )
        print(f"User's car is present -> {result}")
        assert result is True

    def test_check_car_api_test(self):
        current_user_car = self.user_car.session.get(
            url="https://qauto2.forstudy.space/api/cars"
        )
        assert current_user_car.json()["data"][0]["brand"] == "Porsche"

    def teardown_class(self):
        result = self.user_car.session.delete(
            url="https://qauto2.forstudy.space/api/users"
        )
        print(f"\nUser deleted {result}")
        self.add_car1.driver.quit()
