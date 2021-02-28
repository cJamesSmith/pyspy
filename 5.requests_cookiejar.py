import requests
from requests.utils import dict_from_cookiejar

url = 'https://www.baidu.com'

response = requests.get(url)
print(response.cookies)
print(dict_from_cookiejar(response.cookies))
