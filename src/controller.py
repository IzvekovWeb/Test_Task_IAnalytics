
from employee import Employee



def get_employee_work_time(employee_phone):
    employee = Employee.search_by_phone(employee_phone)
    work_time = employee.get_work_time()
    return  work_time

def show_employee_work_time(employee_phone):
    start, end = get_employee_work_time(employee_phone)
    print(f"=== Время работы сотрудника: с {start.strftime('%H:%M')} до {end.strftime('%H:%M')} ===")

def set_employee_work_time(employee, start_time, end_time):
    pass

def set_meet(employee, start_time, end_time):
    pass


    
if __name__ == "__main__":
    show_employee_work_time('79266693217')