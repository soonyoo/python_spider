# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv

class DangdangComPipeline(object):
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

    # 关闭爬虫时顺便将文件保存退出
    def close_spider(self, spider):
        self.file.close()
