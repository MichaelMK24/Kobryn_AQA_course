from Kobryn_AQA_course.lesson_20.pages.add_car_page import AddCarPageInGarage
from Kobryn_AQA_course.lesson_20.pages.garage_page import GaragePage
from Kobryn_AQA_course.lesson_20.pages.login_page import LoginPage
from Kobryn_AQA_course.lesson_20.pages.navigation_bar_page import NavigationBarPage


class BaseFacade:
    def __init__(self):
        self.login_page = LoginPage()
        self.navigation_bar_page = NavigationBarPage()
        self.garage_page = GaragePage()
        self.add_car_page = AddCarPageInGarage()
