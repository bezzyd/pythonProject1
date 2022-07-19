import random

HELP = """
Список доступных команд:
help - напечатать справку по программе
add - добавить задачу в список(название задачи запрашивается у пользователя)
show - показать добавленные задачи
random - добавить случайную задачу дату Сегодня
"""
tasks = {
}
random_tasks = ['Записаться', 'Написать', 'Покормить', 'Помыть']

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print(f'Задача {task} добавлена на дату {date}')

while True:
    command = input('Введите команду\n')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        date = input('Введите дату для добавления задачи: ')
        task = input('Введите название задачи: ')
        add_todo(date, task)
    elif command == 'show':
        date = input('Введите дату для отображения списка задач: ')
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print('Такой даты нет')
    elif command == 'random':
        task = random.choice(random_tasks)
        add_todo('Сегодня', task)
    elif command == 'exit':
        print('Спасибо за использования! До свидания!')
        break
    else:
        print('Неизвестная команда')
        break

