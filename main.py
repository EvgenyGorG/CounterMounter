import os

from dotenv import load_dotenv
import requests


def main():
    load_dotenv()
    service_token = os.getenv('TOKEN')
    url = 'https://rutube.ru/feeds/popular/'
    method = 'method/utils.getShortLink'
    payload = {
        'url': url,
        "access_token": service_token,
        'v': 5.199
    }
    response = requests.get(url + method, params=payload)
    response.raise_for_status()
    print(response.json())

if __name__ == '__main__':
    main()

