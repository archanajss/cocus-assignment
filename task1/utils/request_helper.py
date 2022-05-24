import requests

from config import BASE_URI
from pprint import pprint
from urllib.parse import urljoin

def get(path):
    url = urljoin(BASE_URI, path)
    print('\r\nGET ' + url)
    return requests.get(url)

def post(path, payload, headers):
    url = urljoin(BASE_URI, path)
    print('\r\nPOST ' + url)
    print()
    pprint(payload, indent=2)
    return requests.post(url, data=payload, headers=headers)