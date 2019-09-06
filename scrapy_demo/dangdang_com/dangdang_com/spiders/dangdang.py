# -*- coding: utf-8 -*-
import scrapy

from  dangdang_com.items import DangdangComItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input&page_index=1']

    def parse(self, response):
        lis = response.xpath("//ul[@class='bigimg']/li")
        for li in lis:
            book_url = li.xpath("./a/@href").get()
            yield scrapy.Request(url=book_url, callback=self.parse_detail)

    def parse_detail(self, response):
        # 书名
        book_name = response.xpath("//div[@id='product_info']/div[@class='name_info']/h1/@title").get()
        # 描述
        desc = response.xpath("//div[@id='product_info']/div[@class='name_info']/h2/span/@title").get().strip()
        # 作者
        author = ''.join(response.xpath("//span[@id='author']//text()").getall()).split('作者:')[-1]
        # 出版社
        pub = response.xpath("//div[@class='messbox_info']/span[2]/a/text()").get()
        # 出版时间
        pub_date = response.xpath("//div[@class='messbox_info']/span[3]/text()").get()
        pub_date = pub_date.split('出版时间:')[-1]
        pub_date = ''.join(pub_date.split())
        # 价格
        price = response.xpath("//p[@id='dd-price']/text()").getall()[1].strip()
        item = DangdangComItem(name=book_name,desc=desc,author=author,pub=pub,pub_date=pub_date,price=price)
        yield item
