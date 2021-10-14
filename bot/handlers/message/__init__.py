from telegram.ext import MessageHandler
from telegram.ext.filters import Filters
from bot.handlers.message.text_message import text_message_handlers
from bot.entities import Message

# some of the shared handlers
def prepare_post(update, context):
    new_post = Message(update, context)
    new_post.prepare_post()

shared_message_handlers = [
    MessageHandler(Filters.chat_type.private, callback=prepare_post)
]

message_handlers = text_message_handlers + shared_message_handlers