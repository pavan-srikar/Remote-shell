import os
import telebot

bot_token = '7330784814:AAFa2SnQjUx2JNzNQ7azAOiVGxwhXgQBRBg'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Linux Remote Shell!\nTo run commands, enter the password using /pass <yourpassword> in a private chat with the bot.\nThen, send commands using /cmd <command>.")

@bot.message_handler(commands=['pass'])
def handle_private_command(message):
    password = message.text.split(' ', 1)[1]
    # Save the password for later use
    with open('password.txt', 'w') as file:
        file.write(password)
    bot.reply_to(message, "Password saved. You can now run commands in public chats.")

@bot.message_handler(commands=['cmd'])
def handle_public_command(message):
    command = message.text.split(' ', 1)[1]
    try:
        # Read the saved password
        with open('password.txt', 'r') as file:
            password = file.read().strip()
        
        # Run the command with sudo and the saved password
        output = os.popen(f"echo {password} | sudo -S {command}").read()
        bot.reply_to(message, output)
    except Exception as e:
        bot.reply_to(message, f"Error executing command: {str(e)}")

bot.polling()