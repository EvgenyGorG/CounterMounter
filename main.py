import argparse
import os
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests


def shorten_link(url, token):
    short_link_method = 'https://api.vk.com/method/utils.getShortLink'
    payload = {
        'url': url,
        "access_token": token,
        'v': 5.199
    }
    response = requests.get(short_link_method, params=payload)
    response.raise_for_status()
    short_link_content = response.json()
    short_url = short_link_content['response']['short_url']
    return short_url


def count_clicks(url, token):
    disassembled_link = urlparse(url)
    url = disassembled_link.path.replace('/', '')
    link_stats_method = 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        'key': url,
        "access_token": token,
        'v': 5.199
    }
    response = requests.get(link_stats_method, params=payload)
    response.raise_for_status()
    click_statistics = response.json()
    number_of_clicks = click_statistics['response']['stats'][0]['views']
    return number_of_clicks


def is_shorten_link(url, token):
    check_link_method = 'https://api.vk.com/method/utils.checkLink'
    payload = {
        'url': url,
        "access_token": token,
        'v': 5.199
    }
    response = requests.get(check_link_method, params=payload)
    response.raise_for_status()
    link_status = response.json()
    checked_link = link_status['response']['link']

    return checked_link != url


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Ваша ссылка')

    return parser


def main():
    load_dotenv()
    token = os.environ['VK_SERVICE_TOKEN']
    parser = create_parser()
    args = parser.parse_args()
    url = args.link

    try:
        if is_shorten_link(url, token):
            print('По вашей ссылке перешли', count_clicks(url, token), 'раз')
        else:
            print(shorten_link(url, token))
    except KeyError:
        print('Ошибка, неправильно указана ссылка.')


if __name__ == '__main__':
    main()

