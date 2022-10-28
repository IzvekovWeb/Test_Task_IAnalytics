

from datetime import time

from DB.database import Database


class Calendar():

    def __init__():
        pass

    def get_working_time(self) -> str:
        pass

    def get_free_slots(self) -> list:
        
        pass

    def set_slot(self, start_time: time, end_time: time):
        pass

    
    def create_meet(start_time: time, end_time: time):
        cursor = Database().connect()

        sql = """INSERT INTO meet (start_time, end_time)
                    VALUES (:st, :et)"""
        cursor.execute(sql, {"st": start_time, "et": end_time})
