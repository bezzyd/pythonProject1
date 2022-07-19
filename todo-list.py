HELP = """
Список доступных команд:
* print - напечатать все задачи на заданную дату
* todo - добавить задачу
* help - напечатать help
"""

today = list()
tomorrow = list()
other = list()

while True:
    command = input('Введите команду\n')
    if command == 'help':
        print(HELP)
    elif command == 'todo':
        date = input('Введите дату выполнения задачи: ')
        task = input('Введите задачу')
        if date == 'Сегодня':
            today.append(task)
        elif date == 'Завтра':
            tomorrow.append(task)
        else:
            other.append(task)
        print(f'Задача {task} добавлена')
    elif command == 'show':
        print('Сегодня')
        print(today)
        print('Завтра')
        print(tomorrow)
        print('Другие')
        print(other)
    elif command == 'exit':
        print('Спасибо за использования! До свидания!')
        break
    else:
        print('Неизвестная команда')
        break

