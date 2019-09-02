# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class SinaNewsPipeline(object):
    def __init__(self):
        db_params = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'QAZ123qaz#',
            'database': 'sina_news',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**db_params)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        print('are you ok ? ')
        self.cursor.execute(self.sql, (item['title'], item['pub_time'], item['data_source'], item['content'], item['show_author'], item['keywords'], item['url_source']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into news(title,pub_time,data_source,content,show_author,keywords,url_source) values (%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql
