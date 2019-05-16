# coding: utf-8


import requests


response = requests.get("https://www.12306.cn/mormhweb/", verify=False)
response.encoding = 'utf-8'
print(response.text)
# encoding = response.encoding
# response.encoding = 'ISO-8859-1'
# print(encoding)
# print(response.content.decode('utf-8'))

