from bot.entities.text_message import TextMessage

def text_message(handler_func):
    def wrapper(update, context):
        handler_func(update, context, TextMessage(update, context))
    return wrapper