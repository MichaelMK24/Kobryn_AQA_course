from typing import Union

from Kobryn_AQA_course.lesson_23_sql.alchemy.model.users_model import UsersModel
from Kobryn_AQA_course.lesson_23_sql.alchemy.session import session
from sqlalchemy.exc import IntegrityError


class UsersRepository:

    def __init__(self):
        self.__session = session
        self.__model = UsersModel

    def get_all(self):
        users = self.__session.query(self.__model).all()
        return users

    def get_by_id(self, id: int) -> UsersModel:
        user = self.__session.get(self.__model, {'id': id})
        return user

    def create_new(self, user_model: UsersModel) -> Union[bool, str]:
        try:
            self.__session.add(user_model)
            return True
        except IntegrityError as e:
            self.__session.rollback()
            return str(e)

    def delete_user(self, user_id: int) -> Union[bool, str]:
        try:
            user = self.get_by_id(user_id)
            self.__session.delete(user)
            return True
        except IntegrityError as e:
            self.__session.rollback()
            return str(e)

    def update_user_info(self, id, age, name, country, city, email, password):
        self.__session.query(self.__model).filter(UsersModel.id == id).update({UsersModel.age: age,
                                                                               UsersModel.name: name,
                                                                               UsersModel.country: country,
                                                                               UsersModel.city: city,
                                                                               UsersModel.email: email,
                                                                               UsersModel.password: password})


if __name__ == '__main__':
    repo = UsersRepository()
    # new_user = UsersModel(age=24, name='Monkey D.', country='Spain', city='Madrid', email='monkey@example.com',
    #                       password='basepass2')
    # repo.create_new(new_user)
    # repo.delete_user(9)
    # repo.update_user_info(10, 19, 'Mugiwara', 'Spain', 'Barcelona', 'mugiwara@example.com', 'basepass3')
    print(*repo.get_all(), sep="\n")
    print(f"Get user by id=1: \n{repo.get_by_id(1)}")
