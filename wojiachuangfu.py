# -*- coding: utf-8 -*-
import requests
import time


#全局变量
global telList
telList = []

'''
功能：登陆创富，并推送指定号码列表
时间：2019-1-26
author:xuwenyuan
'''


class ZqhdClient(object):
    def __init__(self):
        object.__init__(self)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'origin': 'zqhd.chainew.com'}
        self.session = requests.session()
        self.session.headers.update(headers)

    # 登陆
    def login(self, username, password):
        url = 'https://zqhd.chainew.com/flowq/front/home/login'
        data = {'phoneNo': username,
                'password': password}
        headers = {'referer': 'https://zqhd.chainew.com/flowq/front/pay/homeIndex',
                   'host': 'zqhd.chainew.com'}

        self.session.post(url, data=data, headers=headers)
        # print(self.session.cookies.items())

    # 推送SMS
    def orderByPhoneBill(self, rebateType, productId, phoneNo, orderFlag, shareFlag):
        url = 'https://zqhd.chainew.com/flowq/front/product/orderByPhoneBill'
        data = {'rebateType': rebateType, 'productId': productId, 'phoneNo': phoneNo, 'orderFlag': orderFlag,
                'shareFlag': shareFlag}
        r = self.session.post(url, data=data)
        # print(r.content.decode('utf-8'))

    #读取txt文件
    def read_txt(self, file_name):
        # f = open('./'+file_name)
        # print(f.read())
        # f.close()
        with open(file_name, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline().replace("\n", "")  # 整行读取数据,并去掉换行符
                if not lines:
                    break
                    pass
                telList.append(lines)  # 添加新读取的数据
                pass
        # print(telList)
        return telList


if __name__ == '__main__':
    c = ZqhdClient()
    # 用户名和密码（密码md5加密）
    c.login('fs1325**', '93D3130470066E4185E246661529AEF7')

    # 读取号码文件(tel.txt文件要与python文件放到同一目录下)
    c.read_txt('./tel.txt')
    for i in telList:
        # 1015591是上面URL产品ID（productId），针对不同产品，要做相应修改
        c.orderByPhoneBill('2', '1015591', i, 'Y', 'N')
        time.sleep(1) #间隔1秒发送1次（时间可调整）
