# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings


class XiciSpiderPipeline(object):
    def __init__(self):
        # 从settings.py中读取键值
        settings = get_project_settings()
        dbkwargs = settings.get("DBKWARGS")
        self.conn = pymysql.connect(**dbkwargs)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        try:
            self.cursor.execute(self.sql, (item['ip'], item['port'], item['position'], item['type'], item['speed'], item['last_check_time']))
            self.conn.commit()
        except Exception as ex:
            print('Insert Error' + str(ex))
            self.conn.rollback()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into proxy(ip,port,position,type,speed,last_check_time) values (%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql
