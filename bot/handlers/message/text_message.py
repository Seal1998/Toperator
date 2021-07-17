from telegram.ext import MessageHandler
from telegram.ext.filters import Filters

def reply_ping(update, context):
    update.message.reply_text(text='pong')

text_handlers = [
    MessageHandler(Filters.text & Filters.regex('ping'), reply_ping)
]