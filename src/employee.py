from datetime import time
from DB.DataBase import DataBase
from psycopg2.extras import RealDictCursor


class Employee():

    def __init__(self, 
                phone: str | None = None, 
                name: str | None = None, 
                surname: str | None = None, 
                position: str | None = None, 
                start_work: time = time(9,0), 
                end_work: time = time(18,0)):
        self.id = None
        self.name = name
        self.surname = surname
        self.position = position
        self.phone = phone
        self.start_work = start_work
        self.end_work = end_work

    def __str__(self):
        return f"""     Данные о работнике:
        ID: {self.id}
        Имя: {self.name}
        Фамилия: {self.surname}
        Должность: {self.position}
        Телефон: {self.phone}
        Начало работы: {self.start_work.strftime('%H:%M')}
        Конец работы: {self.end_work.strftime('%H:%M')}"""
    
    def add(self):
        db = DataBase()
        cur = db.cursor

        sql = """INSERT INTO employee (name, surname, position, phone, start_work, end_work) 
                               VALUES (%s, %s, %s, %s, %s, %s)"""
        cur.execute(sql, (self.name, self.surname, self.position, self.phone, self.start_work, self.end_work))

    def get(self, employee_id):
        db = DataBase()
        cur = db.cursor
        cur = db.conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM employee WHERE employee_id = %s"
        cur.execute(sql, (employee_id, ))

        result = cur.fetchone()
        if result:
            self.id = result['employee_id']
            self.name = result['name']
            self.surname = result['surname']
            self.position = result['position']
            self.phone = result['phone']
            self.start_work = result['start_work']
            self.end_work = result['end_work']

        return self


    @staticmethod
    def get_all_employees():
        db = DataBase()
        cur = db.cursor
        cur = db.conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM employee"
        cur.execute(sql)

        return cur.fetchall()

    @staticmethod
    def search_by_phone(phone: str):
        db = DataBase()
        cur = db.conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM employee WHERE phone=%s"
        cur.execute(sql, (phone, ))

        result = cur.fetchone()
        if result:
            employee = Employee(result['phone'], result['name'], result['surname'], 
                                result['position'],result['start_work'], result['end_work'])
            employee.id = result['employee_id']

            return employee
        return None

    
    def get_work_time(self) -> tuple:
        db = DataBase()
        cur = db.cursor

        sql = "SELECT start_work, end_work FROM employee WHERE employee_id=%s"
        cur.execute(sql, (self.id, ))
        
        user_time = cur.fetchone()
        try:
            start_time = user_time[0]
            end_time = user_time[1]
        except TypeError as e:
            raise TypeError('Сотрудник не найден')
        return (start_time, end_time)

    
if __name__ == "__main__":
    pass
    # Добавим пользователя
    # start = time(10, 00)
    # end = time(19, 00)
    # employee = Employee('79266693218', 'Вика', 'Извекова', 'Бухгалтер',  start, end)
    # employee.add()

    # Employee.get_work_time(1)

    emp = Employee('79266693217')
    emp.get(3)
    print(emp)