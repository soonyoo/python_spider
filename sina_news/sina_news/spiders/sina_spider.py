# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from sina_news.items import SinaNewsItem


class SinaSpiderSpider(CrawlSpider):
    name = 'sina_spider'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'.+/[a-z]{1}/2019-05-08/doc-[0-9a-z]{15}\.shtml'), callback="parse_detail", follow=False),
    )

    def parse_detail(self, response):
        # url_source = response.url
        # print(url_source)
        title = response.xpath("//h1[@class='main-title']/text()").get()
        pub_time = response.xpath("//span[@class='date']/text()").get()
        data_source = response.xpath("//div[@class='date-source']/a/text()").get()
        content = response.xpath("//div[@id='article']").get()
        show_author = response.xpath("//p[@class='show_author']/text()").get()
        keywords = ",".join(response.xpath("//div[@class='keywords']/a/text()").getall())
        url_source = response.url
        item = SinaNewsItem(title=title, pub_time=pub_time, data_source=data_source, content=content, show_author=show_author, keywords=keywords, url_source=url_source)
        yield item
