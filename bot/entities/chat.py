from database import models

class Chat:
    def __init__(self, update, context, chat):
        self.obj = chat
        self.type = self.obj.type
        self.tid = self.obj.id

    def save_chat(self, name):
        saved_channel = models.Chat.add(name, self.obj.id, self.obj.type)
        return saved_channel