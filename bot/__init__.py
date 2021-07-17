from telegram.ext import Updater
from bot.handlers import bot_handlers


def init_updater(token, certificate, private_key):
    updater = Updater(token)
    updater.dispatcher.bot_data['token'] = token
    updater.dispatcher.bot_data['certificate'] = certificate
    updater.dispatcher.bot_data['key'] = private_key
    list(map(updater.dispatcher.add_handler, bot_handlers))
    return updater

def ignite_updater(updater, ip, port):
    updater.start_webhook(  listen='0.0.0.0', 
                            port="8443", 
                            url_path=updater.dispatcher.bot_data['token'], 
                            cert=updater.dispatcher.bot_data['certificate'], 
                            key=updater.dispatcher.bot_data['key'], 
                            webhook_url=f"https://{ip}:{port}/{updater.dispatcher.bot_data['token']}")
