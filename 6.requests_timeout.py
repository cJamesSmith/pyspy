import requests

url = 'https://www.twitter.com'


try:
    response = requests.get(url, timeout=3)
except requests.exceptions.ConnectTimeout as e:
    print(e)