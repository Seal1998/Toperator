from database.models import Chat
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class PostKeyboard:

    def __init__(self):
        self.destination_chats = Chat.get_name_tid_dict()
        self.render_main()

    def render_main(self):
        publish_button = InlineKeyboardButton(text='Publish', callback_data='post_main_publish')
        add_destination_button = InlineKeyboardButton(text='+', callback_data='post_main_dest-new')

        destination_rows = []
        for chat_title, chat_id in self.destination_chats.items():
            destination_rows.append(self.add_main_destination_row(chat_title, chat_id))

        self.markup = InlineKeyboardMarkup([[publish_button], *destination_rows, [add_destination_button]])

    def add_main_destination_row(self, chat_title, chat_id):
            return [
                    InlineKeyboardButton(text=f'{chat_title}', callback_data=f'post_main_NONE_{chat_title}-{chat_id}'),
                    InlineKeyboardButton(text='X', callback_data=f'post_main_dest-delete_{chat_title}-{chat_id}')
                ]