# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql
# # from scrapy.utils.project import get_project_settings
# from xici_spider import settings

import os
from scrapy.exporters import CsvItemExporter


class XiciSpiderPipelineToCSV(object):

    def open_spider(self, spider):
        print("开始输出CSV文件")
        store_file = os.path.dirname(__file__) + '/spiders/xiciData.csv'
        self.file = open(store_file, "wb")
        self.exporter = CsvItemExporter(self.file, fields_to_export=["ip", "port", "position", "type", "speed", "last_check_time"])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        print("结束输出CSV文件")
