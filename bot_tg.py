import telebot
from telebot import types
from random import randint

TOKEN = '6466460772:AAGemdg03MFDS8MaGUEJi4KwUxqNWJ6-On8'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот HUUE!')

    stick = open('../AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sticker=stick)

@bot.message_handler(commands=['hello'])
def hello(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Как дела?')
    btn2 = types.KeyboardButton('Случайное число')
    btn3 = types.KeyboardButton('Что делаешь?')
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id,
                     f'''Привет, {message.from_user.first_name}! 
                     Я бот <b>{bot.get_me().first_name}</b>''',
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def pars_text(message):
    if message.text == 'Как дела?':
        bot.send_message(message.chat.id, 'Нормально, а у тебя?')
    elif message.text == 'Случайное число':
        bot.send_message(message.chat.id, str(randint(83, 100)))
    elif message.text == 'Что делаешь?':

        inline = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton('сижу', callback_data='sit')
        button_2 = types.InlineKeyboardButton('лежу', callback_data='lay')

        inline.add(button_1, button_2)

        bot.send_message(message.chat.id, 'Ничего. А ты?', reply_markup=inline)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'sit':
        bot.send_message(call.message.chat.id, 'ну и сиди')
    elif call.data == 'lay':
        bot.send_message(call.message.chat.id, 'ну и лежи')

bot.polling(non_stop=True)
