import django, pprint
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Nacosbot.settings'
django.setup()
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import Bot
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
from Nacosbot_API.models import *

TOKEN = config('TOKEN')
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
        /materials - materials to all courses
        /lecturers - lecturers and their courses
        /about - Details of the BOT
        """
    )

def start(update, context):
    reply_keyboard = [
        ["/start"],
        ["/location"],
        ["/courses"],
        ["/materials"],
        ["/lecturers"],
        ["/about"],
        ["/help"],
    ]
    update.message.reply_text("Hello! 🙋‍♂️ Welcome to NacossBot use the menu button to select available commands or use the listed options from the keyboard", reply_markup=ReplyKeyboardMarkup(reply_keyboard,))


def location(update, context):
    classes = Classes.objects.all()
    keyboard = [[InlineKeyboardButton(str(pro), callback_data=str(pro.pk))] for pro in classes]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('please select the class you need location details for', reply_markup=reply_markup)

def button(update, context):

    chat_id = update.callback_query.message.chat.id
    query_data = update.callback_query.data
    try:
        loc = Location.objects.get(province_id=query_data)
        context.bot.send_photo(chat_id=chat_id, caption=str(f'{loc.province} is located at: \n{loc}\nRefer to the image of the building ⬆️ for easy identification'), photo= open(loc.image.path, 'rb'))
    except Location.DoesNotExist:
        update.callback_query.message.edit_text('Unable to get Location Details')

        keyboard = [[InlineKeyboardButton(str(pro), callback_data=str(pro.pk))] for pro in Classes.objects.all()]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.callback_query.message.edit_text('Unable to get Location Details \nplease select another class you need location details for', reply_markup=reply_markup)

# Register Commands
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('location', location))

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()