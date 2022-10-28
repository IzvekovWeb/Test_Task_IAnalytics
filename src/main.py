


def main():
    menu = """
    Учёт слотов времени сотрудников

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
                pass
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