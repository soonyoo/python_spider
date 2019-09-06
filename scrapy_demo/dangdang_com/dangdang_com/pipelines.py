# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv
from common.csv_util import CsvUtil


class DangdangComPipeline(object):
    """ 把数据保存在CSV

    1.方法一：逐条写入

    """
    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = os.path.dirname(os.path.dirname(__file__)) + '/dangdang.csv'
        # 打开(创建)文件
        self.file = open(store_file, 'w', encoding='utf_8_sig', newline='')
        # csv写法
        self.csv_header = ['name','desc', 'author', 'pub', 'pub_date','price']
        self.writer = csv.writer(self.file)
        self.writer.writerow(self.csv_header)


    def process_item(self, item, spider):
        # 此处可以加一些判断条件再写csv
        self.writer.writerow((item['name'], item['desc'], item['author'], item['pub'],item['pub_date'],item['price']))
        return item

    # 爬虫结束时，将文件保存退出
    def close_spider(self, spider):
        self.file.close()

class DangdangComPipelineCSV(object):
    """保存csv

    2.批量保存数据

    """
    def __init__(self):
        self.book_info = list()

    def process_item(self, item, spider):
        self.book_info.append(item)
        return item

    def close_spider(self, spider):
        file_full_path = 'D:/python/2019-09-06/dangdang_book.csv'
        csv_header = ['name','desc','author','pub','pub_date','price']
        CsvUtil.create_csv_file(csv_header,self.book_info,file_full_path,False)
