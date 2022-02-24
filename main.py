import telebot
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в бот Рината Гильмиярова. Я демонстрационный бот. \n' +
                     'Отправь команду /hello чтобы получить привественное сообщение'
                     )

@bot.message_handler(commands=['hello'])
def get_text_messages(message):
    username = message.from_user.username
    msg = f'Приветсвую тебя в данном Телеграм боте, {username}'
    bot.send_message(message.chat.id, msg)

bot.polling()