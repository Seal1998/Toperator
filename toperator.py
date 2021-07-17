import yaml
import bot
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--config', '-c', required=True, dest='config')
args = parser.parse_args()

def load_config(config_file):
    with open(config_file, 'r') as config:
        config_dict = yaml.safe_load(config)
    return config_dict

config = load_config(args.config)

updater = bot.init_updater(
        token = config['bot']['token'],
        certificate = './cert.pem',
        private_key = './key.pem')

bot.ignite_updater(updater, '31.202.137.61', '8443')

print(updater.dispatcher.bot_data)