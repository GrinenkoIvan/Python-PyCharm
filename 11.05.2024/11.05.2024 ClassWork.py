#import sqlite3
#
# cars_tpl = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]

# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)

    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

    # for car in cars_tpl:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_tpl)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executescript("""
    # DELETE FROM cars WHERE model LIKE 'B%';
    #
    # UPDATE cars SET price = price + 100;
    # """)



# con.commit() - сохраняет все изменения в БД
# con.close() - закрывает соединение с БД

# try:
#     connection = sqlite3.connect("car.db")
#     cursor = connection.cursor()
#     cursor.executescript("""
#         CREATE TABLE IF NOT EXISTS cars(
#             car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             model TEXT,
#             price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#         UPDATE cars SET price = price + 100;
#         """)
#     connection.commit()
# except sqlite3.Error:
#     if connection:
#         connection.rollback()
#     print('Ошибка выполнения запроса.')
# finally:
#     if connection:
#         connection.close()

# with sqlite3.connect("car.db") as connection:
#     connection.row_factory = sqlite3.Row
#     cursor = connection.cursor()
#     cursor.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT,
#         tr_in INTEGER,
#         buy INTEGER
#     );
#     """)

    # cursor.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    # last_row_id = cursor.lastrowid # id последней записи
    # buy_car_id = 2
    # cursor.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

    # cursor.execute("SELECT model, price FROM cars")
    #
    # # rows =cursor.fetchone()
    # # print(rows)
    # # rows = cursor.fetchall()
    # # print(rows)
    # # rows = cursor.fetchmany(5)
    # # print(rows)
    #
    # for res in cursor:
    #     print(res['model'], res['price'], res[0], res[1])


# def read_avatar(param):
#     try:
#         with open(f'{param}.png', 'rb') as file:
#             return file.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_avatar(name, data):
#     try:
#         with open(name, 'wb') as file:
#             file.write(data)
#     except IOError as e:
#         print(e)
#         # return False
#
#
# with sqlite3.connect("car.db") as connection:
#     connection.row_factory = sqlite3.Row
#     cursor = connection.cursor()
#     cursor.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         avatar BLOB,
#         score INTEGER
#     );
#     """)
#
#     # image = read_avatar(1)
#     #
#     # if image:
#     #     binary = sqlite3.Binary(image)
#     #
#     #     cursor.execute("INSERT INTO users VALUES ('Илья', ?, 1000)", (binary,))
#
#     cursor.execute("SELECT avatar FROM users")
#     image = cursor.fetchone()['avatar']
#     write_avatar("out.png", image)

# with sqlite3.connect("car.db") as connection:
#     cursor = connection.cursor()
#
#     with open('sql_dump.sql', 'w') as file:
#         for sql in connection.iterdump():
#             file.write(sql)

# with sqlite3.connect("car.db") as connection:
#     cursor = connection.cursor()
#
#     with open('sql_dump.sql', 'r') as file:
#         sql = file.read()
#         cursor.executescript(sql)