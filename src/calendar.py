

from datetime import time

from DB.DataBase import DataBase


class Calendar():

    def __init__(self):
        pass

    def get_working_time(self) -> str:
        pass

    def get_free_slots(self) -> list:
        
        pass

    def set_slot(self, start_time: time, end_time: time):
        pass


    @staticmethod
    def create_meet(start_time: time, end_time: time):
        db = DataBase()
        cur = db.cursor

        sql = "INSERT INTO meet (start_time, end_time) VALUES (%s, %s)"
        cur.execute(sql, (start_time, end_time))

    @staticmethod
    def add_meet_to_employee(employee_id, meet_id):
        db = DataBase()
        cur = db.cursor

        sql = "INSERT INTO calendar (employee_id, meet_id) VALUES (%s, %s)"
        cur.execute(sql, (employee_id, meet_id))


if __name__ == "__main__":
    # start = time(15, 30)
    # end = time(16, 50)

    calendar = Calendar()
    # calendar.create_meet(start, end)
