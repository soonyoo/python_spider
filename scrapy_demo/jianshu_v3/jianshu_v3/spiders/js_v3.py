# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_v3.items import ArticleItem


class JsV3Spider(CrawlSpider):
    name = 'js_v3'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

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
        # 数据格式：阅读 164506
        read_count = response.xpath("//span[@class='views-count']/text()").get().split(' ')[-1]
        like_count = response.xpath("//span[@class='likes-count']/text()").get().split(' ')[-1]
        word_count = response.xpath("//span[@class='wordage']/text()").get().split(' ')[-1]
        comment_count = response.xpath("//span[@class='comments-count']/text()").get().split(' ')[-1]
        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item = ArticleItem(
            title=title,
            avatar=avatar,
            article_id=article_id,
            origin_url=origin_url,
            author=author,
            pub_time=pub_time,
            content=content,
            read_count=read_count,
            like_count=like_count,
            word_count=word_count,
            comment_count=comment_count,
            subjects=subjects
        )
        yield item
