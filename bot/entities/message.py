from collections import defaultdict
from database.models import *
from bot.entities.chat import Chat
from bot.keyboards import PostKeyboard

class Message:
    def __init__(self, update, context):
        self.update = update
        self.context = context
        self.message = self.get_message()
        self.chat = Chat(update, context, self.message.chat)
        
    def get_message(self):
        if self.update.message:
            return self.update.message
        elif self.update.channel_post:
            return self.update.channel_post
        elif self.update.callback_query.message:
            return self.update.callback_query.message

    def create_cached_context(self, message_id=None):
        if 'callback' not in self.context.chat_data.keys():
            self.context.chat_data['callback'] = defaultdict(dict)

        cache_key = message_id if message_id != None else self.message.message_id
        self.callback_cache = self.context.chat_data['callback'][f'{cache_key}']

    def delete(self):
        self.message.delete()

    def reply_text(self, text):
        self.message.reply_text(text)

    def prepare_post(self):
        post_keyboard = PostKeyboard()
        post_message_id = self.message.reply_copy(self.chat.tid, self.message.message_id, reply_markup=post_keyboard.markup)['message_id']
        self.create_cached_context(message_id=post_message_id)

        self.callback_cache['keyboard'] = post_keyboard
        self.delete()