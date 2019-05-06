# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from jianshu_v2.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    # https://www.jianshu.com/p/cba0ade531ca

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get()
        url = response.url
        url1 = url.split('?')[0]
        article_id = url1.split('/')[-1]
        origin_url = url
        content = response.xpath("//div[@class='show-content-free']").get()
        item = ArticleItem(
            title=title,
            avatar=avatar,
            article_id=article_id,
            origin_url=origin_url,
            author=author,
            pub_time=pub_time,
            content=content
        )
        yield item
