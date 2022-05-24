import requests

from config import BASE_URI
from urllib.parse import urljoin

def get(path):
    url = urljoin(BASE_URI, path)
    print('\r\nGET ' + url)
    return requests.get(url)
