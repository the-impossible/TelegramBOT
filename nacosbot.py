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
        ["/start ⌚"],
        ["/location 🗺️"],
        ["/courses 📃"],
        ["/materials 📄"],
        ["/lecturers 👤"],
        ["/about 🎯"],
        ["/help 🆘"],
    ]
    update.message.reply_text("Hello! 🙋‍♂️ Welcome to NacossBot use the menu button to select available commands or use the listed options from the keyboard", reply_markup=ReplyKeyboardMarkup(reply_keyboard,))

def location(update, context):
    keyboard = [[InlineKeyboardButton(str(pro), callback_data=f'{pro.pk}-location')] for pro in Classes.objects.all()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('please select the class you need location details for', reply_markup=reply_markup)

def courses(update, context):
    keyboard = [[InlineKeyboardButton(f'{pro} Level', callback_data=f'{pro.pk}-course')] for pro in Level.objects.all()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('please select the Level you need courses for', reply_markup=reply_markup)

def materials(update, context):
    keyboard = [[InlineKeyboardButton(f'{pro} Level', callback_data=f'{pro.pk}-material')] for pro in Level.objects.all()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('<b>please select the Level you need courses Materials for?</b>', reply_markup=reply_markup, parse_mode='HTML')

def about(update, context):
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id, text='This bot provides information regarding the Computer Science department of Kaduna Polytechnic 🏠, information such as courses offered by the department, a list of all the lecturers👥 and their courses, course credit load, lecture materials📄 for download and direction of all computer lecture halls', parse_mode='HTML')

def lecturers(update, context):
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id, text='<b>Computer Science Lecturers 👤</b>', parse_mode='HTML')
    for pro in Lecturer.objects.all():
        details = f'<b>{pro.title}</b> {pro.name}\n<b>Courses: ⬇️\n\n</b>'
        for lec in CoursesToLecturer.objects.filter(lecturer=pro):
            details += f'<b>Title: </b> {lec.course.title}\n<b>Code: </b> {lec.course.code}\n<b>Level: </b> {lec.course.level} Level\n\n'
        context.bot.send_photo(chat_id=chat_id, caption=details, photo= open(pro.pics.path, 'rb'), parse_mode='HTML')

def button(update, context):
    chat_id = update.callback_query.message.chat.id
    query_data = update.callback_query.data.split('-')

    if query_data[1] == 'location':
        try:
            loc = Location.objects.get(province_id=query_data[0])
            context.bot.send_photo(chat_id=chat_id, caption=str(f'{loc.province} is located at: \n{loc}\nRefer to the image of the building above ⬆️ for easy identification'), photo=open(loc.image.path, 'rb'))
        except Location.DoesNotExist:
            keyboard = [[InlineKeyboardButton(str(pro), callback_data=f'{pro.pk}-location')] for pro in Classes.objects.all()]
            reply_markup = InlineKeyboardMarkup(keyboard)

            context.bot.send_message(chat_id=chat_id, text=f'Unable to get Location Details for <b>{Classes.objects.get(id=query_data[0])}</b>\nplease select another class you need location details for', parse_mode='HTML', reply_markup=reply_markup)

    if query_data[1] == 'course':
        keyboard = [[InlineKeyboardButton(f'{pro} Courses', callback_data=f'{pro.pk}-{query_data[0]}-scourse')] for pro in Semester.objects.all()]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=chat_id, text=f'What semester for {Level.objects.get(pk=query_data[0])} Level do you need all the course list for?', reply_markup=reply_markup)

    try:
        if query_data[2] == 'scourse':
            qs = Course.objects.filter(semester=query_data[0], level=query_data[1])
            if qs:
                course_list = f'<b>{qs[0].semester} courses for {qs[0].level} Level</b> ⬇️⬇️\n'
                for pro in qs:
                    course_list += f'\nTitle: {pro.title}\nCode: {pro.code}\nUnit: {pro.unit}\nDescription: {pro.desc}\n\n'
                context.bot.send_message(chat_id=chat_id, text=course_list, parse_mode='HTML')
            else:
                context.bot.send_message(chat_id=chat_id, text=f'Unable to fetch course list for {Semester.objects.get(pk=query_data[0])} {Level.objects.get(pk=query_data[1])} level 🥺')
    except: pass

    if query_data[1] == 'material':
        keyboard = [[InlineKeyboardButton(f'{pro} Courses', callback_data=f'{pro.pk}-{query_data[0]}-smaterial')] for pro in Semester.objects.all()]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=chat_id, text=f'<b>What semester courses for {Level.objects.get(pk=query_data[0])} Level  do you need materials for?</b>', reply_markup=reply_markup, parse_mode='HTML')

    try:
        if query_data[2] == 'smaterial':
            qs = Material.objects.filter(semester=query_data[0], level=query_data[1])
            if qs:
                material_list = f'<b>{qs[0].semester} courses for {qs[0].level} Level</b> ⬇️⬇️'
                context.bot.send_message(chat_id=chat_id, text=material_list, parse_mode='HTML')
                for pro in qs:
                    context.bot.send_document(chat_id=chat_id, filename=pro.file.path, document=open(pro.file.path, 'rb'), caption=f'\nTitle: {pro.course.title}\nCode: {pro.course.code}\nUnit: {pro.course.unit}\nDescription: {pro.course.desc}\n\n')
            else:
                context.bot.send_message(chat_id=chat_id, text=f'Unable to fetch {Semester.objects.get(pk=query_data[0])} courses for {Level.objects.get(pk=query_data[1])} Level 🥺')
    except: pass


# Register Commands
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('location', location))
dispatcher.add_handler(CommandHandler('courses', courses))
dispatcher.add_handler(CommandHandler('materials', materials))
dispatcher.add_handler(CommandHandler('lecturers', lecturers))
dispatcher.add_handler(CommandHandler('about', about))

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()