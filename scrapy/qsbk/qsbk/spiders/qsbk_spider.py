# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        print('='*40)
        print(type(response))
        print('='*40)
