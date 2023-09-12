from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import relationship
from .base import Base


class UsersModel(Base):
    __tablename__ = 'users'
    id = Column(INTEGER, primary_key=True)
    age = Column(INTEGER)
    name = Column(VARCHAR(100))
    country = Column(VARCHAR(100))
    city = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(VARCHAR(100))
    cars = relationship(argument="CarsModel", back_populates="user")

    def __str__(self):
        return f"ID: {self.id} Age: {self.age} Name: {self.name} Country: {self.country} City: {self.city} " \
               f"Email: {self.email} Password: {self.password} Cars: {self.cars}"

    def __repr__(self):
        return f"ID: {self.id} Age: {self.age} Name: {self.name} Country: {self.country} City: {self.city} " \
               f"Email: {self.email} Password: {self.password} Cars: {self.cars}"

