# coding: utf-8
import requests


class ProxyRequests(object):
    def __init__(self):
        self.url = 'http://www.httpbin.org/ip'

    def get_ip(self):
        response = requests.get(self.url)
        print(response.text)

    def get_ip_use_proxy(self):
        proxies = {'HTTP': '47.99.242.42:8080'}
        response = requests.get(self.url, proxies=proxies, timeout=10)
        print(response.text)


if __name__ == '__main__':
    proxy = ProxyRequests()
    # proxy.get_ip()
    print('-----'*10)
    proxy.get_ip_use_proxy()
