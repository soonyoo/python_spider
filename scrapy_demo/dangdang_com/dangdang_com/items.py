# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangComItem(scrapy.Item):
    # 书名
    name = scrapy.Field()
    # 书的描述
    desc = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 出版社
    pub = scrapy.Field()
    # 出版时间
    pub_date = scrapy.Field()
    # 价格
    price = scrapy.Field()
