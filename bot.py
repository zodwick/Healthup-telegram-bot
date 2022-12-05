from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import random

updater = Updater("5843037694:AAH-10MK1PQVE7DEk4v3YDvCljkeAcI2eoM",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"""Hey I hope you're doing well today :)  
		
	How can i help you today:
    press:
    /health tip of the day - cause we care for your health
	/book appointment - get best doctors near you at your fingertips
	/find your medicine -Send us a photo . we'll tell you what medicine it is
	/contact - its free come hangout. we're nice people :)""")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""How can i help you today:
    press:
    /health tip of the day - cause we care for your health
	/book appointment - get best doctors near you at your fingertips
	/find your medicine -Send us a photo . we'll tell you what medicine it is
	/contact - its free come hangout. we're nice people :)""")


def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text("Please do visit our website to upload your photo and find all the info you'll need 🤗  => healthup.com")
	
	
htip=['Base your meals on higher fibre starchy carbohydrates. ...',
'Eat lots of fruit and veg. ...',
'Eat more fish, including a portion of oily fish. ...',
'Cut down on saturated fat and sugar. ...',
'Eat less salt: no more than 6g a day for adults. ...',
'Get active and be a healthy weight. ...',
'Do not get thirsty. ...',
'Do not skip breakfast.']

def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text(random.choice(htip))
	


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Please do visit our website to find the best doctors based on your needs 🤗  => \
		 http://localhost:3002/")


def geeks_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Find your medicine at 🤗  => \
		 http://localhost:3002/")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('health', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('book', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('find', gmail_url))
updater.dispatcher.add_handler(CommandHandler('contact', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
