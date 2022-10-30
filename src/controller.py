
from calendar import Calendar
from employee import Employee



def get_employee_work_time(employee_phone: str):
    employee = Employee.search_by_phone(employee_phone)
    work_time = employee.get_work_time()
    return  work_time

def show_employee_work_time(employee_phone: str):
    start, end = get_employee_work_time(employee_phone)
    print(f"=== Время работы сотрудника: с {start.strftime('%H:%M')} до {end.strftime('%H:%M')} ===")

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
        print('Встреча {meet_id} назначена сотруднику {employee_id}')
    except Exception as e:
        print(f'Возникла ошибка: {e}')

    
if __name__ == "__main__":
    show_all_employees()