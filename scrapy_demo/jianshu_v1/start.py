# coding: utf-8

from scrapy import cmdline
"""
####爬取简书网站####
v1: 普通方式，插入数据库；
v2: 改为插入数据库异步;
v3: 改进：使用selenium,爬取ajax加载的数据
"""

cmdline.execute('scrapy crawl js'.split())
