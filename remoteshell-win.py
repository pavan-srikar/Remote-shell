import os
import telebot

bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Windows Remote Shell!\nTo run commands, send them in a private chat with the bot.")

@bot.message_handler(func=lambda message: message.chat.type == 'private')
def handle_private_command(message):
    command = message.text
    try:
        # Run the command with PowerShell as administrator
        output = os.popen(f"powershell -Command \"& {{ {command} }}\"").read()
        bot.reply_to(message, output)
    except Exception as e:
        bot.reply_to(message, f"Error executing command: {str(e)}")

bot.polling()