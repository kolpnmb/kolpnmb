import telebot
token = '5132176469:AAHLroTt-bMBglESXe-dpyALqHYtHKJksYg'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!". format(message.from_user))

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1= types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо', reply_markup=markup)
    
 @bot.message_handler(content_types='text')
 def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"https://yandex.ru")

if __name__ == '__main__':
     bot.infinity_polling()
