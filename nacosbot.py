from telegram.ext import Updater, CommandHandler
from telegram import Bot

TOKEN = "6053378479:AAEBYjyRwvbbGT7r_830MSuqLm-JK-NlYJY"

bot = Bot(TOKEN)
print(bot.get_me())

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

def help(update, context):
    update.message.reply_text(
        """
        The following commands are available:

        /start - Welcome to NacossBot
        /help - List out all the available commands
        /location - Gives directions to all classes
        /courses - courses  at various levels
        /materials - materials to all courses at various level
        /lecturers - Lists all the lecturers and their courses
        /about - Details of the BOT
        """
    )

def start(update, context):
    update.message.reply_text("Hello! Welcome to NacossBot use the menu button to select available commands")


def location(update, context):
    update.message.reply_text("Location PLENTY!")

# Register Commands
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('location', location))

updater.start_polling()
updater.idle()