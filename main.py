import webbrowser
import telebot

bot = telebot.TeleBot('5926706182:AAGk3M0SxGNLkKxvz-TppnO78bjZcws_B6M')


@bot.message_handler(commands=['site', 'website', 'vk'])
def site(message):
    webbrowser.open('https://vk.com/chakis0')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(
        message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(
        message.chat.id, '<b>Help</b> <em>information</em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(
            message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
