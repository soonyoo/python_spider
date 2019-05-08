# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings


class XiciSpiderPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        DBKWARGS = settings.get("DBKWARGS")
        self.conn = pymysql.connect(**DBKWARGS)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['ip'], item['port'], item['position'], item['type'], item['speed'], item['last_check_time']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into proxy(ip,port,position,type,speed,last_check_time) values (%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql
