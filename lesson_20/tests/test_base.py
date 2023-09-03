from ..facades.Kobryn_HW24 import UserCreatedByApi
from ..constants.url_constants import DEFAULT_URL
from ..facades.garage_facade import GarageFacade
from ..facades.login_facade import LoginFacade
from ..driver.custom_driver import Driver


class TestBase:
    def setup_class(self):
        self.driver = Driver().driver
        self.driver.get(DEFAULT_URL)
        self.users_car = UserCreatedByApi()
        self.users_car.create_user_by_api()
        self.login_facade = LoginFacade()
        self.garage_facade = GarageFacade()
