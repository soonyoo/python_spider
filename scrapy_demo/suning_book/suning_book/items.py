# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningBookItem(scrapy.Item):
    big_category = scrapy.Field()
    middle_category = scrapy.Field()
    small_category = scrapy.Field()
    small_url = scrapy.Field()
    shop_name = scrapy.Field()
    shop_url = scrapy.Field()
    book_url = scrapy.Field()
    book_name = scrapy.Field()
    author = scrapy.Field()
    publishing_house = scrapy.Field()
    publishing_date = scrapy.Field()
    price = scrapy.Field()



