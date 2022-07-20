import telebot

bot = telebot.TeleBot('5426131943:AAFZUjAZOtkGnwgtZsavbK57OAi55Kfl6ts')

HELP = """
Список доступных команд:
/help - вывести список доступных команд
/todo - добавить задачу
/show - показать все задачи на заданную дату
/random - добавить случайную задачу дату
"""

todos = dict()

def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=['show'])
def show(message):
    dates = message.text.split(maxsplit=1)[1].lower().split()
    response = ''
    for date in dates:
        tasks = todos.get(date)
        response += f'{date}: \n'
        for task in tasks:
            response += f'* {task}\n'
        response += '\n'
    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)