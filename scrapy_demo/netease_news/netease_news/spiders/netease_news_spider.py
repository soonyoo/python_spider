# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import time
from netease_news.items import NeteaseNewsItem


class NeteaseNewsSpiderSpider(CrawlSpider):
    name = 'netease_news_spider'
    allowed_domains = ['news.163.com']
    start_urls = ['https://news.163.com/']

    # 当天新闻日期格式处理
    ymd = time.strftime("%Y%m%d", time.localtime())
    yy = ymd[2:4]
    mm_dd = ymd[4:9]
    # https://news.163.com/19/0516/17/EFAK2PV2000189FH.html

    rules = (
        Rule(LinkExtractor(allow=r'https://news.163.com/%s/%s/[0-9]{2}/[A-Z0-9]{16}\.html' % (yy, mm_dd)), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = NeteaseNewsItem()
        item['url_source'] = response.url
        item['website'] = '163'
        item['title'] = response.xpath("//div[@class='post_content_main']/h1/text()").get()
        item['pub_time'] = response.xpath("//div[@class='post_time_source']/text()").get().strip('\n').strip()[0:19]
        item['data_source'] = response.xpath("//a[@id='ne_article_source']/text()").get()
        item['content'] = response.xpath("//div[@id='endText']").get()
        item['show_author'] = response.xpath("//span[@class='ep-editor']/text()").get()
        yield item



