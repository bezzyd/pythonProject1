import telebot
from telebot import types

bot = telebot.TeleBot('5468690642:AAHhm3w2L3xcFPpeAmUZBPKVv_ZQDijAPJQ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    reg_button = types.KeyboardButton('Записаться на занятие')
    about_me_button = types.KeyboardButton('Обо мне')
    instagram_button = types.KeyboardButton('Мой инстаграмм')
    markup.add(reg_button, about_me_button, instagram_button)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text(message):
    week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if message.text == 'Обо мне':
        bot.send_message(message.chat.id, 'Меня зовут Алина. Я инструктор по йоге.'
                                          'Вы можете записаться ко мне на оффлайн занятия в Воронеже,'
                                          'или онлайн с помощью команды "Записаться на занятие"')
    elif message.text == 'Мой инстаграмм':
        bot.send_message(message.chat.id, 'https://catchtherail.ru')
    elif message.text == 'Записаться на занятие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        monday_button = types.KeyboardButton('Понедельник')
        tuesday_button = types.KeyboardButton('Вторник')
        wednesday_button = types.KeyboardButton('Среда')
        thursday_button = types.KeyboardButton('Четверг')
        friday_button = types.KeyboardButton('Пятница')
        saturday_button = types.KeyboardButton('Суббота')
        sunday_button = types.KeyboardButton('Воскресенье')
        main_menu_button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(
            monday_button, tuesday_button, wednesday_button,
            thursday_button, friday_button, saturday_button,
            sunday_button, main_menu_button
                   )
        bot.send_message(message.chat.id, 'На какой день желаете записаться?', reply_markup=markup)
    elif message.text in week_days:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        online_group_reg_button = types.KeyboardButton('Групповое онлайн занятие')
        online_solo_reg_button = types.KeyboardButton('Индивидуальное онлайн занятие')
        offline_group_reg_button = types.KeyboardButton('Групповое оффлайн занятие')
        offline_solo_reg_button = types.KeyboardButton('Индивидуальное оффлайн занятие')
        main_menu_button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(
            online_group_reg_button, online_solo_reg_button, offline_group_reg_button,
            offline_solo_reg_button, main_menu_button)
        bot.send_message(message.chat.id, 'Какой формат занятий вам подходит?', reply_markup=markup)
    elif message.text == 'Групповое онлайн занятие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        main_menu_button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(main_menu_button)
        bot.send_message(message.chat.id, 'К сожалению на эту запись нет свободных мест', reply_markup=markup)
    elif message.text == 'Индивидуальное онлайн занятие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        main_menu_button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(main_menu_button)
        bot.send_message(537998432, 'Прислал сообщение', reply_markup=markup)
        bot.send_message(message.chat.id, 'Вы записались на занятие!', reply_markup=markup)
    elif message.text == 'Групповое оффлайн занятие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        main_menu_button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(main_menu_button)
        bot.send_message(message.chat.id, 'К сожалению на эту запись нет свободных мест', reply_markup=markup)
    elif message.text == 'Индивидуальное оффлайн занятие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        main_menu_button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(main_menu_button)
        bot.send_message(message.chat.id, 'К сожалению на эту запись нет свободных мест', reply_markup=markup)
    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        reg_button = types.KeyboardButton('Записаться на занятие')
        about_me_button = types.KeyboardButton('Обо мне')
        instagram_button = types.KeyboardButton('Мой инстаграмм')
        markup.add(reg_button, about_me_button, instagram_button)
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Такому меня не научили...')

bot.polling(none_stop=True)


