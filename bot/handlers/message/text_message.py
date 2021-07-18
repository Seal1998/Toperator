from telegram.ext import MessageHandler
from telegram.ext.filters import Filters
from bot.handlers.message.decorators import text_message

@text_message
def reply_ping(update, context, text_message=None):
    text_message.reply_text('pong')
    print(text_message.message)

@text_message
def test_process_delete(update, context, text_message=None):
    text_message.delete()

text_handlers = [
    MessageHandler(Filters.text & Filters.regex('ping'), reply_ping),
    MessageHandler(Filters.text & Filters.regex('delete'), test_process_delete)
]