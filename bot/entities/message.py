from database.models import *
from bot.entities.chat import Chat

class Message:
    def __init__(self, update, context):
        self.update = update
        self.message = update.message if update.message else update.channel_post
        self.chat = Chat(update, context)
        
    def delete(self):
        self.message.delete()

    def reply_text(self, text):
        self.message.reply_text(text)

    def prepare_post(self):
        self.message.reply_copy(self.chat.tid, self.message.message_id)
        self.delete()