# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from netease_news import settings
from twisted.enterprise import adbapi
# from pymysql import cursors


class NeteaseNewsPipeline(object):
    def __init__(self):
        db_params = settings.DB_PARAMS
        self.dbpool = adbapi.ConnectionPool('pymysql', **db_params)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                  insert into news(website,title,pub_time,data_source,content,show_author,url_source) values (%s,%s,%s,%s,%s,%s,%s)
                  """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (item['website'], item['title'], item['pub_time'],
                                  item['data_source'], item['content'], item['show_author'],
                                  item['url_source'])
                       )

    def handle_error(self, error, item, spider):
        print('--' * 40)
        print(error)
        print('--' * 40)
