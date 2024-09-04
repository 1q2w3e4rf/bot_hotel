import telebot
import json

message_text = ""

user_ids = []

try:
    config = json.load(open('config.json'))
    message_text = config['message']
    TOKEN = config['TOKEN']
except FileNotFoundError:
    config = {
        'message' : 'change message',
        'TOKEN' : 'change TOKEN'  
    }
    json.dump(config, open('config.json', 'w'), indent=4)

bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(content_types=['text'])
def echo_message(message : telebot.types.Message):
    status = bot.get_chat_member(message.chat.id, message.from_user.id).status
    if status != 'administrator' and status != 'creator' and message_text != ('' or 'change message') and message.from_user.id not in user_ids:
        bot.send_message(message.chat.id, message_text)
        user_ids.append(message.from_user.id)
        


if TOKEN != 'change TOKEN':
    bot.infinity_polling()