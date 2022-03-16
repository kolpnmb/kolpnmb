import telebot
from telebot import types
token = '5132176469:AAHLroTt-bMBglESXe-dpyALqHYtHKJksYg'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!". format(message.from_user))

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1= types.KeyboardButton("vk")
    item2= types.KeyboardButton("instagram")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,'Выберите что вам надо', reply_markup=markup)


if __name__ == '__main__':
     bot.infinity_polling()
