from bot.entities.text_message import TextMessage
from sqlalchemy.sql.expression import text
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from bot.entities.message import Message
import bot.messages as messages

def process_chats(update, context):
    chats_message = Message(update, context)
    if len(context.args) == 1:
        if context.args[0] in ('list', 'ls'):
            chats_message.reply_text(messages.database.chat.all_chats_info())
    chats_message.delete()

info_command_handlers = [
    CommandHandler('chats', process_chats)
]