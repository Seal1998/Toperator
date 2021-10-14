from database.models import Chat

def all_chats_info():
    all_chats = Chat.get_all()
    if all_chats:
        all_chats_string = list(map(str, all_chats))
        return '\n'.join(all_chats_string)
    else:
        return False