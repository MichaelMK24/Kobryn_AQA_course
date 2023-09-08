import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='Admin24',
    host='127.0.0.1',
    port='5432',
    database='20_05AQA_Group'
)

cursor = connection.cursor()

a = cursor.execute("SELECT * FROM users")  # відправляє запит в базу данних
# print(cursor.fetchall())
print(cursor.fetchone())
b = 0

