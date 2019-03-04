# -*- coding: utf-8 -*-
import scrapy
# from scrapy.http.response.html import HtmlResponse
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_url = "https://www.qiushibaike.com"

    def parse(self, response):
        # 返回SelectorList
        article_divs = response.xpath('//div[@id="content-left"]/div')
        for article_div in article_divs:
            # 每个article_div的数据类型是Selector
            author = article_div.xpath('.//div[@class="author clearfix"]//h2/text()').get()
            # 获取所有指定div下面的文本
            content = article_div.xpath('.//div[@class="content"]//text()').getall()
            # 把文本连起来(join)并去空格
            content = "".join(content).strip()
            # 使用items.py中定义的字段来接收
            item = QsbkItem()
            item['author'] = author
            item['content'] = content
            yield item
        # 多页数据的爬取(如果只爬一页，上面就OK了，如果还要爬多页，则要用下面的代码)
        # next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        # if not next_url:
        #     return
        # else:
        #     yield scrapy.Request(self.base_url+next_url, callback=self.parse)
