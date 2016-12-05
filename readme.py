import telebot

TOKEN = '313443008:AAENH71oMNUG6IULxcwP7r-BJd48ClnPPec'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'www')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Privet, {name}. QQQ.'.format(name=message.text))

bot.polling()