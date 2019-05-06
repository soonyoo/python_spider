# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class JianshuV1Pipeline(object):
    def __init__(self):
        db_params = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'QAZ123qaz#',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**db_params)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['article_id'], item['origin_url']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(title,content,author,avatar,pub_time,article_id,origin_url) values (%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql



