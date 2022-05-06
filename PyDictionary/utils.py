import requests
from bs4 import BeautifulSoup

def _get_soup_object(url, user_proxies, parser="html.parser"):
    if user_proxies is not None:
        return BeautifulSoup(requests.get(url, proxies=user_proxies).text, parser)
    return BeautifulSoup(requests.get(url).text, parser)
