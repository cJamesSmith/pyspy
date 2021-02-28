import requests

url = 'http://www.baidu.com'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'
# print(response.text)
# print(response.encoding)
print(response.content.decode('utf-8'))
print(len(response.content.decode('utf-8')))