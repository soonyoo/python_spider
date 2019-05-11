# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi
from pymysql import cursors
from jianshu_v2 import settings

"""
date:2019-05-10
author:xuwenyuan
desc:Scrapy基于Mysql数据库异步写入数据库 (同步写入，参见v1版本) 。
"""


class JianshuTwistedPipeline(object):
    def __init__(self):

        # db_params = {
        #     'host': '127.0.0.1',
        #     'user': 'root',
        #     'password': 'QAZ123qaz#',
        #     'database': 'jianshu',
        #     'charset': 'utf8',
        #     'cursorclass': cursors.DictCursor
        # }
        db_params = settings.DB_PARAMS
        self.dbpool = adbapi.ConnectionPool('pymysql', **db_params)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                  insert into article(title,content,author,avatar,pub_time,article_id,origin_url) values (%s,%s,%s,%s,%s,%s,%s)
                  """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (
            item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['article_id'],
            item['origin_url']))

    def handle_error(self, error, item, spider):
        print('--' * 40)
        print(error)
        print('--' * 40)

