import os
import telebot

bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the macOS Remote Shell!\nTo run commands with administrative privileges, send them in a private chat with the bot.")

@bot.message_handler(func=lambda message: message.chat.type == 'private')
def handle_private_command(message):
    command = message.text
    try:
        # Run the command with macOS shell with administrative privileges
        output = os.popen(f"sudo {command}").read()
        bot.reply_to(message, output)
    except Exception as e:
        bot.reply_to(message, f"Error executing command: {str(e)}")

bot.polling()