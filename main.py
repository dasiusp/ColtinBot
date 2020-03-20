from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler

from telegram import Update, Bot

from time import sleep

import os


def start(bot, update):
    update.message.reply_text("Coé família, cheguei!", quote=False)
    

def msg(bot, update):
    update.message.reply_text("O Colman já falou que Kotlin é a melhor linguagem hoje?", quote=False)
    sleep(1)
    update.message.reply_text("JÁ DESGRAÇAAAAAAA", quote=False)


def unknown(bot, update):
    update.message.reply_text("Que po#@ de comando é esse ai, Marreco?", quote=False)

                              
def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    
    dispatcher = Dispatcher(bot, None, 0)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('kotlin', msg))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
	
    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'
 
