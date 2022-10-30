

from datetime import time
from DB.DataBase import DataBase
from psycopg2.extras import RealDictCursor, DictCursor

class Calendar():

    @staticmethod
    def create_meet(start_time: time, end_time: time, name: str = None) -> int:
        db = DataBase()
        cur = db.cursor

        sql = "INSERT INTO meet (start_time, end_time, meet_name) VALUES (%s, %s, %s) RETURNING meet_id"
        cur.execute(sql, (start_time, end_time, name))
        meet_id = cur.fetchone()[0]
        return meet_id
    
    @staticmethod
    def get_all_meets():
        db = DataBase()
        cur = db.cursor
        cur = db.conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM meet"
        cur.execute(sql)

        return cur.fetchall()

    @staticmethod
    def add_meet_to_employee(employee_id, meet_id):
        db = DataBase()
        cur = db.cursor
        
        sql = "INSERT INTO calendar (employee_id, meet_id) VALUES (%s, %s)"
        cur.execute(sql, (employee_id, meet_id))

    def check_is_slot_free(employee_id, meet_id):
        db = DataBase()
        cur = db.cursor

        sql = "SELECT start_time, end_time FROM meet WHERE meet_id=%s"
        cur.execute(sql, (meet_id, ))
        meet_time = cur.fetchone()

        free_slots = Calendar.get_free_employee_slots(employee_id)
        for slot_time in free_slots:
            if meet_time[0] >= slot_time[0] and meet_time[1] <= slot_time[1]:
                return True
        return False


    def get_free_employee_slots(employee_id) -> tuple:
        db = DataBase()
        cur = db.cursor
        cur = db.conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT e.start_work, e.end_work FROM employee as e WHERE e.employee_id = %s"
        cur.execute(sql, (employee_id, ))
        employee_work_time = cur.fetchone()

        cur = db.conn.cursor(cursor_factory=DictCursor)
        sql2 = """SELECT m.start_time, m.end_time
                    FROM meet as m JOIN calendar as c ON m.meet_id=c.meet_id
                    WHERE c.employee_id = %s
                    ORDER BY m.start_time"""
        cur.execute(sql2, (employee_id, ))
        meets = cur.fetchall()

        free_slots = []
        if meets:
            last_time = employee_work_time['start_work']
            for meet in meets:
                free_slots.append(tuple([last_time, meet[0]]))
                last_time = meet[1]
        else:
            free_slots.append(tuple([employee_work_time['start_work'], employee_work_time['end_work']]))
            
        return free_slots
    
    def show_free_eployee_slots(slots: tuple):
        print('\n--- Свободные временные слоты сотрудника: ---')
        for slot in slots:
                print(f"c {slot[0].strftime('%H:%M')} до {slot[1].strftime('%H:%M')}")
        



if __name__ == "__main__":
    pass
    # calendar = Calendar()

    # start = time(15, 30)
    # end = time(16, 50)
    # calendar.create_meet(start, end, 'Собрание')


    # start = time(13, 00)
    # end = time(14, 10)
    # calendar.create_meet(start, end, 'Планёрка')

    # --------------    

    # print(Calendar.check_is_slot_free(1, 6))
