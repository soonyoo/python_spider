# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaNewsItem(scrapy.Item):
    title = scrapy.Field()
    pub_time = scrapy.Field()
    data_source = scrapy.Field()
    content = scrapy.Field()
    show_author = scrapy.Field()
    keywords = scrapy.Field()
    url_source = scrapy.Field()

