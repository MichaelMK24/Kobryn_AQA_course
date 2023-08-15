from Kobryn_AQA_course.lesson_20.Kobryn_HW24 import UserCreatedByApi
from Kobryn_AQA_course.lesson_20.constants.url_constants import DEFAULT_URL
from Kobryn_AQA_course.lesson_20.facades.garage_facade import GarageFacade
from Kobryn_AQA_course.lesson_20.facades.login_facade import LoginFacade
from Kobryn_AQA_course.lesson_20.driver.custom_driver import Driver


class TestBase:
    def setup_class(self):
        self.driver = Driver().driver
        self.driver.get(DEFAULT_URL)
        self.users_car = UserCreatedByApi()
        self.users_car.create_user_by_api()
        self.login_facade = LoginFacade()
        self.garage_facade = GarageFacade()
