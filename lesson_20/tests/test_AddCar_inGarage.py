import allure
from allure_commons.types import AttachmentType
from ..constants.api_url_constants import (
    DELETE_USERS_ACCOUNT, GET_USER_CARS,
)
from ..constants.url_constants import DEFAULT_API_URL
from .test_base import TestBase
from ..driver.custom_driver import Driver


def decorator_screenshot(func):
    driver = Driver().driver

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="FAILED TEST SCREEN",
                          attachment_type=AttachmentType.PNG)
            raise

    return wrapper


@allure.suite("Add Car To Garage Tests")
class TestAddCarTest(TestBase):
    def setup_class(self):
        super().setup_class(self)

    @allure.link(url="https://qauto2.forstudy.space/", name="Testing site link")
    @allure.feature("Stable selenium test")
    @decorator_screenshot
    def test_check_car_selenium_test(self):
        self.login_facade.login_full_cycle()
        allure.attach(self.driver.get_screenshot_as_png(), name="Completed 'Log in' form",
                      attachment_type=AttachmentType.PNG)

        self.garage_facade.add_car_to_garage_full_cycle()
        allure.attach(self.driver.get_screenshot_as_png(), name="Filled out 'Add a car' form",
                      attachment_type=AttachmentType.PNG)

        result = self.garage_facade.get_porsche_cayenne_label_from_garage_page()
        allure.attach(self.driver.get_screenshot_as_png(), name="Car that was added to garage",
                      attachment_type=AttachmentType.PNG)

        print(f"User's car is present -> {result}")
        assert result is True

    @allure.link(url="https://qauto2.forstudy.space/api-docs", name="API docs(swagger) link")
    @allure.feature("Stable api test")
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
