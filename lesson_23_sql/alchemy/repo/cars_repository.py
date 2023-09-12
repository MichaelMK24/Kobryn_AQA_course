from typing import Union

from Kobryn_AQA_course.lesson_23_sql.alchemy.model.cars_model import CarsModel
from Kobryn_AQA_course.lesson_23_sql.alchemy.session import session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import literal


class CarsRepository:
    def __init__(self):
        self.__session = session
        self.__model = CarsModel

    def get_all(self):
        cars = self.__session.query(self.__model).all()
        return cars

    def get_car_by_id(self, car_id: int) -> CarsModel:
        car = self.__session.get(self.__model, {'car_id':  car_id})
        return car

    def get_cars_by_brand(self, brand: str):
        cars = self.__session.query(self.__model).filter_by(brand=brand).all()
        return cars

    def create_new(self, car_model: CarsModel) -> Union[bool, str]:
        try:
            self.__session.add(car_model)
            return True
        except IntegrityError as e:
            self.__session.rollback()
            return str(e)

    def delete_car(self, car_id: int) -> Union[bool, str]:
        try:
            car = self.get_car_by_id(car_id)
            self.__session.delete(car)
            return True
        except IntegrityError as e:
            self.__session.rollback()
            return str(e)

    def update_car_info(self, car_id, user_id, brand, model, mileage):
        self.__session.query(self.__model).filter(CarsModel.car_id == car_id).update({CarsModel.user_id: user_id,
                                                                                      CarsModel.brand: brand,
                                                                                      CarsModel.model: model,
                                                                                      CarsModel.mileage: mileage})

    def get_cars_with_mileage_below(self, mileage_threshold: int):
        cars = self.__session.query(self.__model).filter(CarsModel.mileage < literal(mileage_threshold)).all()
        return cars


if __name__ == '__main__':
    car_repo = CarsRepository()
    # new_car = CarsModel(user_id=10, brand='Skoda', model='SuperB', mileage=31572)
    # car_repo.create_new(new_car)
    # car_repo.delete_car(11)
    car_repo.update_car_info(11, 10, 'Audi', 'A6', 23572)
    print(*car_repo.get_all(), sep="\n")
    print(f"Get car by id=8: \n{car_repo.get_car_by_id(8)}")
    print(f"Cars with mileage below 40k:")
    print(*car_repo.get_cars_with_mileage_below(40000), sep="\n")
