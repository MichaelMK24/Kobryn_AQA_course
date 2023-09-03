from ..pages.add_car_page import AddCarPageInGarage
from ..pages.garage_page import GaragePage
from ..pages.login_page import LoginPage
from ..pages.navigation_bar_page import NavigationBarPage


class BaseFacade:
    def __init__(self):
        self.login_page = LoginPage()
        self.navigation_bar_page = NavigationBarPage()
        self.garage_page = GaragePage()
        self.add_car_page = AddCarPageInGarage()
