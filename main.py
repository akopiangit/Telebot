import telebot
from telebot import types

bot = telebot.TeleBot('1054799903:AAHkke7SVb20qSS_QcDvfr_M1ItVlKdMW9E')


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://itproger.com"))
    bot.send_message(message.chat.id,
                     "Отличный выбор, нажмите на кнопку ниже и начинайте изучения курсов прямо сейчас",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['insta'])
def instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com/itproger_official/"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['vk'])
def vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить группу Вк", url="https://vk.com/prog_life"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Меню')
    btn2 = types.KeyboardButton('Доставка')
    btn3 = types.KeyboardButton('Забронировать столик')
    btn4 = types.KeyboardButton('Контакты')
    btn5 = types.KeyboardButton('Оставтиь отзыв')
    btn6 = types.KeyboardButton('Instagram')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_mess = f"<b>Этот бот поможет вам забронировать столик, посмотреть меню, заказать доставку и оставить отзыв! С любовью, Максима Пицца :revolving_hearts:</b>!"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Меню')
        btn2 = types.KeyboardButton('Доставка')
        btn3 = types.KeyboardButton('Забронировать столик')
        btn4 = types.KeyboardButton('Контакты')
        btn5 = types.KeyboardButton('Оставтиь отзыв')
        btn6 = types.KeyboardButton('Instagram')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        final_message = "."
    elif get_message_bot == "меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        f = open("Menu.pdf", "rb")
        bot.send_document(message.chat.id, f)
        final_message = "Наше меню"
    elif get_message_bot == "доставка":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Наш сайт", url="delivery.maxima-pizza.ru"))
        final_message = "Закажите на сайте"
    # Здесь различные дополнительные проверки и условия
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Меню')
        btn2 = types.KeyboardButton('Доставка')
        btn3 = types.KeyboardButton('Забронировать столик')
        btn4 = types.KeyboardButton('Контакты')
        btn5 = types.KeyboardButton('Оставтиь отзыв')
        btn6 = types.KeyboardButton('Instagram')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
