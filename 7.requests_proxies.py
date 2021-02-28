import requests
proxy_ip = '159.75.45.177'
proxy_port = '53076'
proxies = {
    'http': '127.0.0.1:2080',
    'https': '127.0.0.1:2080',
}

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

response = requests.get('https://www.google.com',
                        proxies=proxies,
                        timeout=3,
                        headers=header)
print(response.content.decode())
