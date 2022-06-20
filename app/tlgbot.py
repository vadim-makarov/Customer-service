# from app import bot
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     id_message = f'Your ID is {message.chat.id}'
#     bot.reply_to(message, id_message)
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
#
#
# bot.infinity_polling()
