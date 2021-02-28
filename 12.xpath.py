import requests
from lxml import etree

class Tieba():
    def __init__(self, name):
        self.url = 'https://tieba.baidu.com/f?kw=' + name
        self.headers = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 88.0 .4324 .182 Safari / 537.36 Edg / 88.0 .705 .74'
        }

    def get_data(self, url):
        res = requests.get(url, headers=self.headers)
        return res.content.decode('utf').replace('<!--', '').replace('-->', '')

    def parse_data(self, data):
        html = etree.HTML(data)
        title = html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/text()')
        link = html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href')
        next_url = html.xpath('//a[contains(text(),"下一页")]/@href')
        data_loader = []
        for t, l in zip(title, link):
            data_loader.append({'title': t, 'link': self.url + l})
        print(data_loader)
        return data_loader, next_url

    def run(self):
        while True:
            data = self.get_data(self.url)
            data_loader, next_url = self.parse_data(data)
            if next_url is None:
                break
            self.url = 'https:' + next_url[0]

if __name__ == '__main__':
    tieba = Tieba('浙江大学')
    tieba.run()