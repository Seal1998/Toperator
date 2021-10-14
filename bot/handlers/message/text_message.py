from telegram.ext import MessageHandler
from telegram.ext.filters import Filters
from bot.entities import TextMessage
import bot.messages as messages

def reply_ping(update, context):
    text_message = TextMessage(update, context)
    text_message.reply_text('pong')

def test_process_delete(update, context):
    text_message = TextMessage(update, context)
    text_message.delete()

def debug(update, context):
    print(messages.database.chat.all_chats_info())

text_message_handlers = [
    MessageHandler(Filters.text & Filters.regex('ping'), reply_ping),
    MessageHandler(Filters.text & Filters.regex('delete'), test_process_delete),
    MessageHandler(Filters.text & Filters.regex('debug'), debug)]