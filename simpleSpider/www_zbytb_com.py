# coding = utf-8
import requests
from lxml import etree
import json
from pymongo import MongoClient
import pymongo


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
        self.dataset = self.db.zb_tb

    def get_html_from_url(self):
        """
        从URL获取网页源码
        :return:
        """
        response = requests.get(self.url, headers=self.headers)
        return response.text

    @staticmethod
    def dump_save_file(json_string, file_name, coding):
        """
        使用dump函数，保存文件
        # json.dump(json_string, fp) 这样写会中文乱码，
        # 如果要保存含有中文的字符串，建议加上ensure_ascii=False,json.dump默认使用ascii字符码

        :param json_string: 要保存的json字符串
        :param file_name: 要保存的文件名称
        :param coding: 字符编码(如utf-8)
        :return: 没有返回值
        """
        with open(file_name, 'w', encoding=coding) as fp:
            json.dump(json_string, fp, ensure_ascii=False)

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
        html = etree.HTML(html)
        trs = html.xpath("//table[@class='zblist_table']/tr")[1:]

        biao_dict = dict()
        biao_lists = []
        for tr in trs:
            tds = tr.xpath('./td')
            biao_dict['area'] = tds[0].xpath('./a/text()')[0]
            biao_dict['title'] = tds[1].xpath('./a/text()')[0]
            biao_dict['date_time'] = tds[3].xpath('./text()')[0]
            biao_lists.append(biao_dict)
            biao_dict = {}

        return biao_lists


if __name__ == '__main__':
    pass

    # zhaobiao = ZhaoBiaoWang()
    # lis = zhaobiao.get_data()
    # 1.print输出
    # for li in lis:
    #     print(lis)
    # 2.保存成json文件
    # ZhaoBiaoWang.dump_save_file(lis, 'biao.json', 'utf-8')
    # 3.保存到mongoDB
    # zhaobiao.insert_many(lis)


