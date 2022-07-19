HELP = """
help - напечатать справку по программе
add - добавить задачу в список(название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
"""

run = True

tasks = []
today = []
tomorrow = []
other = []

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks, today, tomorrow, other)
    elif command == 'add':
        when = input('Введите дату выполнения задачи: ')
        if when == 'Сегодня':
            task = input('Введите название задачи: ')
            today.append(task)
        elif when == 'Завтра':
            task = input('Введите название задачи: ')
            tomorrow.append(task)
        elif when not in 'Сегодня' and when not in 'Завтра':
            task = input('Введите название задачи: ')
            other.append(task)
        print('Задача добавлена')
    elif command == 'exit':
        print('Спасибо за использования! До свидания!')
        break
    else:
        print('Неизвестная команда')
        break

