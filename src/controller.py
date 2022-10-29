
from calendar import Calendar
from employee import Employee



def get_employee_work_time(employee_phone: str):
    employee = Employee.search_by_phone(employee_phone)
    work_time = employee.get_work_time()
    return  work_time

def show_employee_work_time(employee_phone: str):
    start, end = get_employee_work_time(employee_phone)
    print(f"=== Время работы сотрудника: с {start.strftime('%H:%M')} до {end.strftime('%H:%M')} ===")

def add_meet_to_employee(employee, start_time, end_time):
    pass

def create_meet(start_time, end_time, name: str | None = None):
    
    meet_id = Calendar.create_meet(start_time, end_time, name)

    return meet_id


    
if __name__ == "__main__":
    show_employee_work_time('79266693217')