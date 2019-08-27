# -*- coding: utf-8 -*-
import scrapy
from tangshi300.items import Tangshi300Item
from copy import deepcopy


class TangshiSpider(scrapy.Spider):
    name = 'tangshi'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org/gushi/tangshi.aspx']

    def parse(self, response):
        tangshi_items = Tangshi300Item()
        spans = response.xpath("//div[@class='typecont']//span")
        for span in spans:
            tangshi_items["author"] = span.xpath('./text()').get()
            tangshi_items["title"] = span.xpath('./a/text()').get()
            tangshi_items['url'] = span.xpath('./a/@href').get()
            yield scrapy.Request(url=tangshi_items['url'], meta={'item': deepcopy(tangshi_items)}, callback=self.parse_tangshi_content)

    def parse_tangshi_content(self, response):
        item = response.meta['item']
        contents = response.xpath("//div[@class='contson']")[0].xpath(".//text()").getall()
        item['contents'] = ''.join(contents)
        yield item
