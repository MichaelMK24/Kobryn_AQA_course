from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Kobryn_AQA_course.lesson_20.pages.base_page import BasePage
from Kobryn_AQA_course.lesson_20.ui_elements.text_box import TextBox
from Kobryn_AQA_course.lesson_20.ui_elements.button import Button


class AddCarPageInGarage(BasePage):
    def __init__(self):
        super().__init__()

        self.brand_select_dropdown = lambda: Button(
            self._driver.find_element(By.ID, "addCarBrand")
        )

        self.brand_select = lambda: Button(
            WebDriverWait(self._driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//option[text()='Porsche']"))
            )
        )

        self.model_select_dropdown = lambda: Button(
            self._driver.find_element(By.ID, "addCarModel")
        )

        # get element after explicitly waiting for 1 seconds
        self.model_select = lambda: Button(
            WebDriverWait(self._driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//option[text()='Cayenne']"))
            )
        )

        self.mileage_field = lambda: TextBox(
            self._driver.find_element(By.ID, "addCarMileage")
        )

        self.add_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Add']")
        )
