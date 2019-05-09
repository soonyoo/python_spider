# -*- coding: utf-8 -*-
import scrapy

from tmall_spider_v1.items import TmallSpiderV1Item


class TmallSpiderSpider(scrapy.Spider):
    name = 'tmall_spider'
    allowed_domains = ['tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%C5%AE%D7%B0&type=p&spm=a220m.1000858.a2227oh.d100']

    def parse(self, response):
        divs = response.xpath("//div[@id='J_ItemList']/div[@class='product  ']/div")
        if not divs:
            self.log("List Page error--%s" % response.url)
        for div in divs:
            item = TmallSpiderV1Item()
            item['goods_price'] = div.xpath("./p[@class='productPrice']/em/@title").get()
            item['goods_name'] = div.xpath("./p[@class='productTitle']/a/@title").get()
            good_url = div.xpath("./p[@class='productTitle']/a/@href").get()
            if 'https' not in good_url:
                good_url = 'https:'+good_url
            item['goods_url'] = good_url
            yield scrapy.Request(url=good_url, meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']
        item['shop_name'] = response.xpath("//div[@class='slogo']/a[@class='slogo-shopname']/strong/text()").get()
        shop_url = response.xpath("//div[@class='slogo']/a[@class='slogo-shopname']/@href").get()
        if 'https' not in shop_url:
            shop_url = 'https:' + shop_url
        item['shop_url'] = shop_url
        yield item





