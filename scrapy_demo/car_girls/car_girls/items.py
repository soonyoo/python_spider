# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarGirlsItem(scrapy.Item):
    brand = scrapy.Field()
    images_num = scrapy.Field()
    girls_name = scrapy.Field()
    image_urls = scrapy.Field()  # image_urls属性
    images = scrapy.Field()  # image属性
