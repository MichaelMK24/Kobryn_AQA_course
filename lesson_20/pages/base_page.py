from Kobryn_AQA_course.lesson_20.driver.custom_driver import Driver


class BasePage:
    def __init__(self):
        self._driver = Driver().driver
