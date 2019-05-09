# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from tmall_spider_v1 import settings
import uuid


class TmallSpiderV1Pipeline(object):
    def __init__(self):
        dbkwargs = settings.DBKWARGS
        self.conn = pymysql.connect(**dbkwargs)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        # print(item)
        try:
            self.cursor.execute(self.sql, (uuid.uuid1(), item['goods_price'], item['goods_name'], item['goods_url'], item['shop_name'], item['shop_url']))
            self.conn.commit()
        except Exception as ex:
            print('Insert Error' + str(ex))
            self.conn.rollback()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into goods(id,goods_price,goods_name,goods_url,shop_name,shop_url) values (%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql
