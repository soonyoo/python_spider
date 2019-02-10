# -*- coding: utf-8 -*-
# 方法1：使用 JsonItemExporter
# from scrapy.exporters import JsonItemExporter
#
#
# class QsbkPipeline(object):
#
#     def __init__(self):
#         self.fp = open('duanzi.json', 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('爬虫结束。。。。')

# 方法2：使用 JsonLinesItemExporter
from scrapy.exporters import JsonLinesItemExporter


class QsbkPipeline(object):

    def __init__(self):
        self.fp = open('duanzi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        # self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        # self.exporter.finish_exporting()
        self.fp.close()
        print('爬虫结束。。。。')
