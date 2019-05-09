# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallSpiderV1Item(scrapy.Item):
    goods_price = scrapy.Field()
    goods_name = scrapy.Field()
    goods_url = scrapy.Field()
    shop_name = scrapy.Field()
    shop_url = scrapy.Field()
    # company_name = scrapy.Field()
    # company_address = scrapy.Field()

