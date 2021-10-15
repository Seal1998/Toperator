from bot.entities.message import Message
from bot.keyboards import PostKeyboard

class CallbackMessage(Message):
    
    def __init__(self, update, context):
        super().__init__(update, context)
        print(self.context.chat_data)
        self.obj = self.update.callback_query
        self.data_parts = self.obj.data.split('_')

        self.create_cached_context()
        self.check_keyboard_cache()
        
    def check_keyboard_cache(self):
        if 'keyboard' not in self.callback_cache.keys():
            if self.data_parts[0] == 'post':
                self.callback_cache['keyboard'] = PostKeyboard()

    def handle(self):
        namespace = self.data_parts[0]
        level = self.data_parts[1]
        action = self.data_parts[2]

        print(namespace, level, action)
