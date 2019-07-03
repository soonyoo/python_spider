# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyttMovieItem(scrapy.Item):
    # 电影标题
    title = scrapy.Field()
    # 海报
    poster = scrapy.Field()
    # 电影裁图
    screen_shot = scrapy.Field()
    # 下载地址
    download_url = scrapy.Field()
    # ◎译　　名
    translated_name = scrapy.Field()
    # ◎年　　代
    year = scrapy.Field()
    # ◎产　　地
    country = scrapy.Field()
    # ◎类　　别
    category = scrapy.Field()
    # ◎语　　言
    language = scrapy.Field()
    # ◎豆瓣评分
    douban_rating = scrapy.Field()
    # ◎片　　长
    duration = scrapy.Field()
    # director
    director = scrapy.Field()
    # actors
    actors = scrapy.Field()
    # 简介
    profile = scrapy.Field()


