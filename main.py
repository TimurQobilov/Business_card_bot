import telebot
from telebot import types


API_TOKEN = '7054224938:AAFSzsPWgYo-UlnFI_RkmqhtO6dYWNOXWT0'
bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_button = types.KeyboardButton('Информация обо мне')
    projects_button = types.KeyboardButton('Мои проекты')
    markup.add(info_button, projects_button)
    bot.send_message(message.chat.id, "Привет! Выберите опцию:", reply_markup=markup)

# Обработчик для текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Информация обо мне':
        show_info_menu(message)
    elif message.text == 'Мои проекты':
        bot.send_message(message.chat.id, 'Вот ссылка на моего бота: https://github.com/TimurQobilov')
    elif message.text == 'Биография':
        bot.send_message(message.chat.id, 'ФИО: Кабилов Тимур\nВозраст: 33\nПол: Мужской')
    elif message.text == 'Образование':
        bot.send_message(message.chat.id, 'Техникум')
    elif message.text == 'Назад':  # Добавляем обработку кнопки "Назад"
        send_welcome(message)

# Меню с кнопками "Биография" и "Образование"
def show_info_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    biography_button = types.KeyboardButton('Биография')
    education_button = types.KeyboardButton('Образование')
    back_button = types.KeyboardButton('Назад')
    markup.add(biography_button, education_button, back_button)
    bot.send_message(message.chat.id, 'Выберите раздел:', reply_markup=markup)

# Запуск бота
bot.polling()