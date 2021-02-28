import requests
import re


def login():
    sess = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    }
    url1 = 'https://github.com/login'
    res1 = sess.get(url1, headers=headers).content.decode()
    token = re.findall('name="authenticity_token" value="(.*?)"', res1)[0]
    time_stamp = re.findall('name="timestamp" value="(.*?)"', res1)[0]
    time_stamp_secret = re.findall(
        'name="timestamp_secret" value="(.*?)"', res1)[0]
    require_code = re.findall('<input type="text" name="(.*?)" hidden="hidden" class="form-control" />', res1)[0]
    print(token, str(time_stamp), str(time_stamp_secret), require_code)

    data = {
        'commit': 'Sign in',
        'authenticity_token': token,
        'login': 'chenbin123.ok@163.com',
        'password': 'Woaiitch0602',
        'trusted_device': '',
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'unsupported',
        'return_to': '',
        'allow_signup': '',
        'client_id': '',
        'integration': '',
        require_code: '',
        'timestamp': str(time_stamp),
        'timestamp_secret': str(time_stamp_secret)
    }
    url2 = 'https://github.com/session'
    res2 = sess.post(url2, data=data, headers=headers).content.decode()

    url3 = 'https://github.com/cJamesSmith'
    res3 = sess.get(url3, headers=headers).content
    with open('github_sess.html', 'wb') as f:
        f.write(res3)


if __name__ == '__main__':
    login()
