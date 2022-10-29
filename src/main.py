


from datetime import time
from controller import create_meet, show_employee_work_time


def main():
    menu = """\nУчёт слотов времени сотрудников
    1. Рабочее время сотрудника
    2. Свободные слоты сотрудника
    3. Создать встречу
    4. Назначить встречу сотруднику
    5. Выйти
    """
    while True:
        print(menu)
        answer = input("Выберите дейсиве (номер): ")
        match answer:
            case '1':
                phone = input('Номер телефона сотрудника (79266693217): ')
                show_employee_work_time(phone)
            case '2':
                pass
            case '3':
                try:
                    name = input("Название: ") or None
                    start = time.fromisoformat(input("Начало (формат: 11:30): "))
                    end = time.fromisoformat(input("Конец (формат: 12:00): "))

                    if start >= end:
                        raise ValueError("Время окончания встречи, не может быть '<=' начала.")
                    
                    meet_id = create_meet(start, end, name)
                    print(f'=== Встреча создана. ID встречи: {meet_id}')

                except IOError as e:
                    print(f'Ошибка ввода данных: {e}')
                except ValueError as e:
                    print(f'Ошибка: Неверный формат времени! {e}')
            case '4':
                # add_meet_to_employee()
                pass
            case '5':
                break

if __name__ == "__main__":
    main()
    print('Программа завершена')
    exit(0)