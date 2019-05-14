# coding： utf-8
import requests


class LoginRenRen(object):
    def __init__(self):
        self.url = 'http://www.renren.com/PLogin.do'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        }
        self.session = requests.Session()
        self.data = {'email': 'soonyoo@126.com', 'password': '666666,./'}
        self.profile = 'http://www.renren.com/425519674/profile'

    def login_renren(self):
        self.session.post(self.url, headers=self.headers, data=self.data)
        response = self.session.get(self.profile)
        html = response.content.decode('utf-8')
        with open('renren.html', 'w', encoding='utf-8') as fp:
            fp.write(html)
        # print(html)


if __name__ == '__main__':
    login = LoginRenRen()
    login.login_renren()





