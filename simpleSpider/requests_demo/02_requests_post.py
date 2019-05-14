# coding: utf-8
import requests


class RequestPost(object):

    def __init__(self):
        self.url = 'http://www.httpbin.org/post'
        self.data = {
            'first': "true",
            'pn': '1',
            'kd': 'python'
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        }

    def parser(self):
        response = requests.post(self.url, data=self.data, headers=self.headers)
        print(type(response.json()))
        print(response.json())


if __name__ == '__main__':
    request = RequestPost()
    request.parser()
