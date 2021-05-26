import requests
import config


def get_msg():
    get_update_url = f'https://api.telegram.org/bot{config.botToken}/getUpdates'
    response = requests.get(get_update_url)
    data = response.text
    return data


def send_msg(msg):
    send_msg_url = f'https://api.telegram.org/bot{config.botToken}/sendMessage?chat_id={config.groupChatID}&text={msg}'
    response = requests.get(send_msg_url)
