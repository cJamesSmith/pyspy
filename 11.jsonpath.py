import  requests
from jsonpath import jsonpath
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

res = requests.get(url, headers=headers).content
# print(res)
dict_data = json.loads(res)
cities = jsonpath(dict_data, '$..name')
print(cities)