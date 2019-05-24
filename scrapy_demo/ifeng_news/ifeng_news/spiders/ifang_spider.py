# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ifeng_news.items import IfengNewsItem


class IfangSpiderSpider(CrawlSpider):
    name = 'ifang_spider'
    allowed_domains = ['news.ifeng.com']
    start_urls = ['https://news.ifeng.com/']
    # https://news.ifeng.com/c/7mrQorB5lol
    # https://news.ifeng.com/c/7mra4XWYJn6
    rules = (
        Rule(LinkExtractor(allow=r'.*/c/[0-9a-zA-Z]{11}'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = IfengNewsItem()
        item['url'] = response.url
        yield item
