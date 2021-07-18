from bot.entities.text_message import TextMessage
from sqlalchemy.sql.expression import text
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from bot.entities.message import Message

def process_start(update, context):
    update.message.reply_text('Howdy!')

def process_text_command(update, context):
    command_message = Message(update, context)
    message_text_parts = command_message.message.text.split()
    context.args = message_text_parts[1:]
    command = message_text_parts[0][1:]
    
    if command == 'toperator':
        process_toperator(update, context)

def process_toperator(update, context):
    toperator_message = Message(update, context)
    if len(context.args) == 1:
        if context.args[0] == 'init':
            if toperator_message.chat.type in ('channel', 'group'):
                toperator_message.chat.save_chat(toperator_message.chat.obj.title)
    toperator_message.delete()

base_command_handlers = [
    CommandHandler('start', process_start),
    CommandHandler('toperator', process_toperator),
    MessageHandler(Filters.text & Filters.regex('^\/'), process_text_command)
]