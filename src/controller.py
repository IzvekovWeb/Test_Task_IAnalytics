
from calendar import Calendar
from employee import Employee


def show_employee_info(employee_id):
    employee = Employee()
    employee.get(employee_id)
    print(employee_id)

def get_employee_by_phone(phone):
    employee = Employee.search_by_phone(phone)
    if employee:
        return employee
    return '=== Пользователя с таким телефоном нет в базе ==='

def get_employee_work_time(employee_id):
    employee = Employee()
    employee.get(employee_id)
    work_time = employee.get_work_time()
    return work_time

def show_employee_work_time(employee_id):
    try:
        start, end = get_employee_work_time(employee_id)
        print(f"=== Время работы сотрудника: с {start.strftime('%H:%M')} до {end.strftime('%H:%M')} ===")
    except TypeError as e:
        print(f"Ошибка: {e.args[0]}")
def create_meet(start_time, end_time, name: str | None = None):
    meet_id = Calendar.create_meet(start_time, end_time, name)
    return meet_id

def show_all_meets():
    meets = Calendar.get_all_meets()
    print('\n==== Доступные встречи: ====')
    print('ID:   | Начало:  | Конец:   | Название: ')
    for meet in meets:
        print(f"{meet['meet_id']}    |  {meet['start_time'].strftime('%H:%M')}   |  {meet['end_time'].strftime('%H:%M')}   |   {meet['meet_name']}")
    print('============================\n')
        
def show_all_employees():
    employees = Employee.get_all_employees()
    print('\n==== Сотрудники: ====')
    print('ID - Имя - Фамилия - Телефон - Должность - Начало - Конец  ')
    print('__________________________________________________________')
    for emp in employees:
        print(f"{emp['employee_id']} - {emp['name']} - {emp['surname']} - {emp['phone']} - {emp['position']} - {emp['start_work']} - {emp['end_work']}")
    print('=====================\n')


def add_meet_to_employee(employee_id, meet_id):
    try:
        Calendar.add_meet_to_employee(employee_id, meet_id)
        print(f'Встреча {meet_id} назначена сотруднику {employee_id}')
    except Exception as e:
        print(f'Возникла ошибка: {e}')

def show_free_employee_slots(employee_id):
    slots = Calendar.get_free_employee_slots(employee_id)
    Calendar.show_free_eployee_slots(slots)


    
if __name__ == "__main__":
    show_all_employees()