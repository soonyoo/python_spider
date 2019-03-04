# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
from datetime import datetime
import re

class BossPipeline(object):
    def __init__(self):
        file_name = 'boss_zhiping_' + re.sub('[.\-:\s]', '', str(datetime.now()))[0:12] + '.json'
        self.fp = open(file_name, 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
        self.x = 0

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        self.x += 1
        print('第%s条记录导入成功' % self.x)
        return item

    def close_spider(self, spider):
        self.fp.close()
