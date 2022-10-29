from datetime import time
from DB.DataBase import DataBase
from psycopg2.extras import RealDictCursor


class Employee():

    def __init__(self, 
                phone: str, 
                name: str | None = None, 
                surname: str | None = None, 
                position: str | None = None, 
                start_work: time | None = None, 
                end_work: time | None = None):
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

    @staticmethod
    def search_by_phone(phone: str):
        db = DataBase()
        cur = db.conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM employee WHERE phone=%s"
        cur.execute(sql, (phone, ))

        result = cur.fetchone()

        employee = Employee(result['phone'], result['name'], result['surname'], 
                            result['position'],result['start_work'], result['end_work'])
        employee.id = result['employee_id']

        return employee

    
    def get_work_time(self) -> tuple:
        db = DataBase()
        cur = db.cursor

        sql = "SELECT start_work, end_work FROM employee WHERE employee_id=%s"
        cur.execute(sql, (self.id, ))
        
        user_time = cur.fetchone()
        start_time = user_time[0]
        end_time = user_time[1]

        return (start_time, end_time)

    
if __name__ == "__main__":
    pass
    # Добавим пользователя
    # start = time(9, 00)
    # end = time(18, 00)
    # employee = Employee('Саша', 'Извеков', 'Программист', '79266693217', start, end)
    # employee.add()

    # Employee.get_work_time(1)

    # emp = Employee('79266693217')
    # print(emp.search_by_phone('79266693217'))