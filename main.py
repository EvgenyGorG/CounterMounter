import os
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests


def shorten_link(url, token):
    method = 'https://api.vk.com/method/utils.getShortLink'
    payload = {
        'url': url,
        "access_token": token,
        'v': 5.199
    }
    response = requests.get(method, params=payload)
    response.raise_for_status()
    method_info = response.json()
    short_url = method_info['response']['short_url']
    return short_url


def count_clicks(url, token):
    parsed = urlparse(url)
    url = parsed.path.replace('/', '')
    method = 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        'key': url,
        "access_token": token,
        'v': 5.199
    }
    response = requests.get(method, params=payload)
    response.raise_for_status()
    method_info = response.json()
    number_of_clicks = method_info['response']['stats'][0]['views']
    return number_of_clicks


def is_shorten_link(url, token):
    method = 'https://api.vk.com/method/utils.checkLink'
    payload = {
        'url': url,
        "access_token": token,
        'v': 5.199
    }
    response = requests.get(method, params=payload)
    response.raise_for_status()
    method_info = response.json()
    checked_link = method_info['response']['link']

    if checked_link != url:
        return True

    return False


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    url = input('Введите ссылку для сокращения: ')

    try:
        if is_shorten_link(url, token):
            print(count_clicks(url, token))
        else:
            print(shorten_link(url, token))
    except KeyError:
        print('Ошибка, неправильно указана ссылка.')


if __name__ == '__main__':
    main()

