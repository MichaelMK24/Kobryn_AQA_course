import allure
from allure_commons.types import AttachmentType
from ..constants.cars_mileage import CARS_MILEAGE
from .base_facade import BaseFacade


class GarageFacade(BaseFacade):
    def __init__(self):
        super().__init__()

    def click_and_fill_all_fields_on_add_car_form(
        self, mileage=CARS_MILEAGE, is_click=True
    ):
        self.click_brand_select_dropdown_from_add_car_page()

        self.click_brand_select_from_add_car_page()

        self.click_model_select_dropdown_from_add_car_page()

        self.click_model_select_from_add_car_page()

        self.fill_in_mileage_field_from_add_car_page(mileage)

        if is_click:
            self.click_add_button_from_add_car_page()

    @allure.step("Add Car to Garage full cycle")
    def add_car_to_garage_full_cycle(self, mileage=CARS_MILEAGE):
        self.click_add_car_button_from_garage_page()
        self.click_and_fill_all_fields_on_add_car_form(mileage)

    def click_brand_select_dropdown_from_add_car_page(self):
        self.add_car_page.brand_select_dropdown().click()

    @allure.step("Select car brand")
    def click_brand_select_from_add_car_page(self):
        self.add_car_page.brand_select().click()
        allure.attach(self.add_car_page._driver.get_screenshot_as_png(), name="Choose car brand from dropdown",
                      attachment_type=AttachmentType.PNG)

    def click_model_select_dropdown_from_add_car_page(self):
        self.add_car_page.model_select_dropdown().click()

    @allure.step("Select car model")
    def click_model_select_from_add_car_page(self):
        self.add_car_page.model_select().click()

    @allure.step("fill_in_mileage_field")
    def fill_in_mileage_field_from_add_car_page(self, mileage):
        self.add_car_page.mileage_field().send_keys(mileage)

    def click_add_button_from_add_car_page(self):
        self.add_car_page.add_button().click()

    def click_add_car_button_from_garage_page(self):
        self.garage_page.add_cars_button().click()

    def get_porsche_cayenne_label_from_garage_page(self):
        return self.garage_page.porsche_cayenne_label()
