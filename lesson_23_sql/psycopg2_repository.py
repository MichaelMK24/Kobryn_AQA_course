import psycopg2


class BaseRepository:

    def __init__(self):
        self.connection = psycopg2.connect(
            user='postgres',
            password='Admin24',
            host='127.0.0.1',
            port='5432',
            database='20_05AQA_Group'
        )
        self.connection.set_session(autocommit=True)
        self._cursor = self.connection.cursor()


class UsersRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def get_all(self):
        self._cursor.execute("SELECT * FROM users")
        return self._cursor.fetchall()

    def insert_into(self, age, name, country, city, email, password):
        self._cursor.execute(f"INSERT INTO users(age, name, country, city, email, password) "
                             f"VALUES ('{age}', '{name}', '{country}', '{city}', '{email}', '{password}');")
        # self.connection.commit()

    def delete_data(self, id):
        self._cursor.execute(f"DELETE FROM users WHERE users.id = {id};")
        # self.connection.commit()


if __name__ == '__main__':
    repo = UsersRepository()
    # repo.insert_into(32, 'Juan Perez', 'Spain', 'Madrid', 'juan.perez@example.com', 'basepass1')
    repo.delete_data(8)
    print(repo.get_all())

