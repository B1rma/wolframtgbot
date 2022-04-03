from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import urllib.parse

from telegram.message import Message
tgbotkey = "" # https://t.me/botfather
wolframappid = "" # https://products.wolframalpha.com/short-answers-api/documentation/
def start_callback(update, context):
    update.message.reply_text("Hello! Write something what you want to know")
def question(update, context):
    line = 'http://api.wolframalpha.com/v1/result?appid=' + wolframappid + '&i=' + urllib.parse.quote(update.message.text)
    response = requests.get(line)
    update.message.reply_text(response.content.decode("utf-8"))

updater = Updater(tgbotkey)

handler = MessageHandler(Filters.text, question)
updater.dispatcher.add_handler(handler)
updater.dispatcher.add_handler(CommandHandler("start", start_callback))

updater.start_polling()
updater.idle()
