from Kobryn_AQA_course.lesson_20.constants.api_url_constants import (
    GET_USER_CARS,
    DELETE_USERS_ACCOUNT,
)
from Kobryn_AQA_course.lesson_20.constants.url_constants import DEFAULT_API_URL
from Kobryn_AQA_course.lesson_20.tests.test_base import TestBase


class TestAddCarTest(TestBase):
    def setup_class(self):
        super().setup_class(self)

    def test_check_car_selenium_test(self):
        self.login_facade.login_full_cycle()
        self.garage_facade.add_car_to_garage_full_cycle()
        result = self.garage_facade.get_porsche_cayenne_label_from_garage_page()

        print(f"User's car is present -> {result}")
        assert result is True

    def test_check_car_api_test(self):
        current_user_car = self.users_car.session.get(
            url=f"{DEFAULT_API_URL}{GET_USER_CARS}"
        )
        assert current_user_car.json()["data"][0]["brand"] == "Porsche"

    def teardown_class(self):
        result = self.users_car.session.delete(
            url=f"{DEFAULT_API_URL}{DELETE_USERS_ACCOUNT}"
        )
        print(f"\nUser deleted {result}")
        self.driver.quit()
