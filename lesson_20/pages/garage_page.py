from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from ..ui_elements.button import Button


class GaragePage(BasePage):
    def __init__(self):
        super().__init__()

        self.add_cars_button = lambda: Button(
            WebDriverWait(self._driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Add car']"))
            )
        )

        self.porsche_cayenne_label = lambda: WebDriverWait(self._driver, 2).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//p[text()='Porsche Cayenne']"), "Porsche Cayenne"
            )
        )
