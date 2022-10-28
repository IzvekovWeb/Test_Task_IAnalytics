import psycopg2

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DataBase:

    def __init__(self):
        self.conn, self.cursor = self.connect()

    @classmethod
    def connect(cls):
        try:
            connection = psycopg2.connect(
                user='sasiz',
                password='12345678',
                host='127.0.0.1',
                port='5432'
            )
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # Курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            print("Соединение с PostgreSQL открыто")
            return connection, cursor
        except (Exception, Error) as e:
            print("Ошибка при работе с PostgreSQL", e)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            self.conn.close()
            print("Соединение с PostgreSQL закрыто")


if __name__ == '__main__':
    db = DataBase()
    db.create_tables()