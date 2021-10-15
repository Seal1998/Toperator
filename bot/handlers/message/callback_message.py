from telegram.ext import CallbackQueryHandler
from telegram.ext.filters import Filters
from bot.entities import CallbackMessage

def post_callback(update, context):
    callback_message = CallbackMessage(update, context)
    callback_message.handle()
    

callback_message_handlers = [
    CallbackQueryHandler(pattern='^post_*', callback=post_callback)
]