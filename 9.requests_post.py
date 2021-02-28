import requests
import json


class King(object):
    def __init__(self, word):
        self.url = 'https://ifanyi.iciba.com/index.php?c=trans'
        self.headers = headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '20',
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'Host': 'ifanyi.iciba.com',
            'Origin': 'https://www.iciba.com',
            'Referer': 'https://www.iciba.com/',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        }
        self.data = {
            'from': 'zh',
            'to': 'en',
            'q': word
        }

    def get_data(self):
        response = requests.post(
            self.url, data=self.data, headers=self.headers)
        return response.content

    def parse_data(self, data):
        dict_data = json.loads(data)
        print(dict_data['out'])
        # return dict_data['out']

    def run(self):
        response = self.get_data()
        self.parse_data(response)


if __name__ == '__main__':
    word = input('翻译啥？')
    king = King(word)
    king.run()
