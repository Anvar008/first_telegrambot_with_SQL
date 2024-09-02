import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_table(
            id INT UNIQUE,
            fullname VARCHAR(255)
            )
        """)
        self.db.commit()

    def insert_into_table(self, user_id, user_fullname):
        self.cursor.execute("""
        INSERT or IGNORE INTO USER_TABLE(id, fullname)
        VALUES(?, ?)
        """, (user_id, user_fullname))
        self.db.commit()

    def select_from_table(self):
        data = self.cursor.execute("""
        SELECT * FROM USER_TABLE
        """)
        return data.fetchall()

    def create_food_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS foods(
            name VARCHAR(255) unique, 
            price INT
            )
        """)
        self.db.commit()

    def select_food_table(self):
        data2 = self.cursor.execute("""
        SELECT * FROM foods
        GROUP BY name
        """)
        return data2.fetchall()

    def insert_food_table(self, name, price):
        self.cursor.execute("""
        INSERT or IGNORE INTO foods(name, price)
        VALUES(?, ?)
        """, (name, price))
        self.db.commit()

    def delete_data(self):
        self.cursor.execute("""
        DELETE FROM foods
        WHERE name='Pizza'
        """)
        self.db.commit()

    def drop_table(self):
        self.cursor.execute("""
        DROP TABLE 
        """)
        self.db.commit()

    def create_drinks_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS drinks_table(
            name VARCHAR(255),
            price INT
            )
        """)
        self.db.commit()

    def add_drinks_table(self, name, price):
        self.cursor.execute("""
        INSERT or IGNORE INTO drinks_table(name, price)
        VALUES(?, ?)
        """, (f"{name}", f"{price}"))
        self.db.commit()

    def select_drinks_table(self):
        data = self.cursor.execute("""
        SELECT * FROM drinks_table
        """)
        return data.fetchall()

    def close_connection(self):
        self.db.close()
