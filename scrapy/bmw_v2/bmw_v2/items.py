# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BmwV2Item(scrapy.Item):
    category = scrapy.Field()
    image_urls = scrapy.Field()  # image_urls属性
    images = scrapy.Field()  # image属性
