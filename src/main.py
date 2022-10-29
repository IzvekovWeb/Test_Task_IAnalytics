


from controller import show_employee_work_time


def main():
    menu = """\nУчёт слотов времени сотрудников
    1. Рабочее время сотрудника
    2. Свободные слоты сотрудника
    3. Добавить встречу
    4. Выйти
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
                pass
            case '4':
                break

if __name__ == "__main__":
    main()
    print('Программа завершена')
    exit(0)