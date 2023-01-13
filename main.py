from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
import os
import argparse

def shorten_link(token, url):
    body = {"long_url": url}
    headers = {"Authorization": token}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=body)
    response.raise_for_status()
    link = response.json().get('link')
    return link


def count_clicks(token, bitlink):
    parsed_link = urlparse(bitlink)
    link = f'{parsed_link.netloc}{parsed_link.path}'
    headers = {"Authorization": token}
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary', headers=headers)
    response.raise_for_status()
    total_clicks = response.json().get('total_clicks')
    return total_clicks


def is_bitlink(token, url):
    parsed_link = urlparse(url)
    link = f'{parsed_link.netloc}{parsed_link.path}'
    headers = {"Authorization": token}
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}', headers=headers)
    return response.ok


def parse_argument():
    parser = argparse.ArgumentParser(
        description='''Программа создает короткую ссылку на URL через серевис BitLi 
        или выводит количество преходов по ссылке, если передается bitli-ссылка'''
    )
    parser.add_argument('url', help='Ссылка на ресурс')
    args = parser.parse_args()
    return args.url


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    user_link = parse_argument()
    if is_bitlink(token, user_link):
        print(count_clicks(token, user_link))
    else:
        print(shorten_link(token, user_link))


if __name__ == '__main__':
    main()
