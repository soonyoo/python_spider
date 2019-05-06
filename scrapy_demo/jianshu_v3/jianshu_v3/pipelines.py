# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
from pymysql import cursors
import uuid


class JianshuTwistedPipeline(object):
    def __init__(self):
        db_params = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'QAZ123qaz#',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **db_params)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                  insert into article_v2(id,title,content,author,avatar,pub_time,article_id,origin_url,read_count,like_count,word_count,comment_count,subjects) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                  """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (str(uuid.uuid1()), item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['article_id'], item['origin_url'], item['read_count'], item['like_count'], item['word_count'], item['comment_count'], item['subjects']))

    def handle_error(self, error, item, spider):
        print('--' * 40)
        print(error)
        print('--' * 40)