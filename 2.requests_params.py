import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
url = 'https://www.baidu.com/s?'
params = {
    'wd': 'python'
}
response = requests.get(url, headers=headers, params=params)

with open('baidu.html', 'wb') as f:
    f.write(response.content)
