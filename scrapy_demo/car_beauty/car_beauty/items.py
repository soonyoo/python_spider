# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarBeautyItem(scrapy.Item):
    brand = scrapy.Field()
    num = scrapy.Field()
    mm_name = scrapy.Field()

    # 使用imagePipline一定要有以下两个字段
    image_urls = scrapy.Field()  # image_urls属性
    images = scrapy.Field()  # image属性

