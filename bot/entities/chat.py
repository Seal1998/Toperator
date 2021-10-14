from database import models

class Chat:
    def __init__(self, update, context):
        self.message = update.message if update.message else update.channel_post
        self.obj = self.message.chat
        self.type = self.obj.type

    def save_chat(self, name):
        saved_channel = models.Chat.add(name, self.obj.id, self.obj.type)
        return saved_channel