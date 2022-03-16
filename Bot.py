import telebot
token = '5132176469:AAHLroTt-bMBglESXe-dpyALqHYtHKJksYg'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!".format(message.from_user))

if __name__ == '__main__':
     bot.infinity_polling()
