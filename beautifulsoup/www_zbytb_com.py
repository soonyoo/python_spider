# coding=utf-8

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient


class ZhaoBiaoWang(object):
    def __init__(self):
        self.url = 'https://www.zbytb.com/gongcheng/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                        ' Chrome/71.0.3578.98 Safari/537.36'}
        # ###MongoDB ###
        self.ip = 'localhost'
        # 端口为int类型
        self.port = 27017
        self.conn = MongoClient(self.ip, self.port)
        self.db = self.conn.zb_db
        self.dataset = self.db.zb_bs4_tb

    def get_html_from_url(self):
        """
        从URL获取网页源码
        :return:
        """
        response = requests.get(self.url, headers=self.headers)
        return response.text

    def insert_many(self, list_dic):
        """
        MongoDB 插入多条数据
        :param list_dic: 数据字典
        :return:
        """
        return self.dataset.insert_many(list_dic)

    def get_data(self):
        """
        获取数据
        :return:
        """
        html = self.get_html_from_url()
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('table', attrs={'class': 'zblist_table'})
        trs = table.find_all('tr')[1:]
        biao_dict = dict()
        biao_lists = []
        for tr in trs:
            infos = list(tr.stripped_strings)
            # print(infos)
            # break
            biao_dict['area'] = infos[0]
            biao_dict['title'] = infos[1]
            biao_dict['date_time'] = infos[2]
            biao_lists.append(biao_dict)
            biao_dict = {}
        return biao_lists

    def get_data_ex(self):
        base_url = 'https://www.zbytb.com/gongcheng-{}.html'
        biao_dict = dict()
        biao_lists = []

        for x in range(1, 5):
            url = base_url.format(x)
            response = requests.get(url, headers=self.headers)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            table = soup.find('table', attrs={'class': 'zblist_table'})
            trs = table.find_all('tr')[1:]
            for tr in trs:
                infos = list(tr.stripped_strings)
                biao_dict['area'] = infos[0]
                biao_dict['title'] = infos[1]
                biao_dict['date_time'] = infos[2]
                biao_lists.append(biao_dict)
                biao_dict = {}

        return biao_lists


if __name__ == '__main__':
    biao = ZhaoBiaoWang()
    biao_list = biao.get_data()

    for biao in biao_list:
        print(biao)

    # 3.保存到mongoDB
    # biao_list = biao.get_data_ex()
    # biao.insert_many(biao_list)
