from bot.handlers.message.text_message import text_handlers
from bot.handlers.command.base_command import base_command_handlers

bot_handlers = base_command_handlers + text_handlers # + something else ...