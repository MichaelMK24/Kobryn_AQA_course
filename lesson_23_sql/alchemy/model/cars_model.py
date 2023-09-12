from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from Kobryn_AQA_course.lesson_23_sql.alchemy.model.users_model import UsersModel


class CarsModel(Base):
    __tablename__ = 'cars'
    car_id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    brand = Column(VARCHAR(100))
    model = Column(VARCHAR(100))
    mileage = Column(INTEGER)
    user = relationship(argument='UsersModel', back_populates='cars')

    def __repr__(self):
        return f"Car_id: {self.car_id} Brand: {self.brand} Model: {self.model} " \
               f"Mileage: {self.mileage} user: {self.user.name}"
