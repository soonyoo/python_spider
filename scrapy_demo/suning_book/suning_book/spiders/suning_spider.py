# -*- coding: utf-8 -*-
import scrapy
from suning_book.items import SuningBookItem
from copy import deepcopy


class SuningSpiderSpider(scrapy.Spider):
    name = 'suning_spider'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        book_item = SuningBookItem()
        menu_items = response.xpath("//div[@class='menu-list']/div[@class='menu-item']")
        menu_subs = response.xpath("//div[@class='menu-list']/div[@class='menu-sub']/div[@class='submenu-left']")
        for i, menu_item in enumerate(menu_items):
            # 书籍大类
            book_item['big_category'] = menu_item.xpath("./dl/dt/h3/a/text()").get()
            # 书籍中类(有些有，有些没有)
            p_list = menu_subs[i].xpath("./p")
            if p_list is not None:
                for p_tag in p_list:
                    book_item['middle_category'] = p_tag.xpath("./a/text()").get()
                    small_list = p_tag.xpath("./following-sibling::ul[1]/li")
                    for small_li in small_list:
                        book_item['small_category'] = small_li.xpath("./a/text()").get()
                        book_list_url = small_li.xpath("./a/@href").get()
                        book_item['small_url'] = book_list_url
                        yield scrapy.Request(url=book_list_url, meta={'item': deepcopy(book_item)}, callback=self.parse_book_list)
                        # yield scrapy.Request(url=book_item['small_url'],  meta={'item': book_item}, callback=self.parse_book_list)

    def parse_book_list(self, response):
        item = response.meta['item']
        lis = response.xpath("//div[@id='filter-results']/ul/li")
        for li in lis:
            item['shop_name'] = li.xpath(".//div[@class='res-info']/p[@class='seller oh no-more ']/@salesname").get()
            shop_url = li.xpath(".//div[@class='res-info']/p[@class='seller oh no-more ']/@producturl").get()

            # 添加https
            if 'http' not in shop_url:
                if 'www' in shop_url:
                    shop_url = 'http:' + shop_url
                else:
                    shop_url = 'https:' + shop_url

            item['shop_url'] = shop_url

            item['book_name'] = li.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/text()").get().strip('\n')

            book_url = li.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/@href").get()
            # 添加https
            if 'http' not in book_url:
                if 'www' in book_url:
                    book_url = 'http:' + book_url
                else:
                    book_url = 'https:' + book_url
            item['book_url'] = book_url
            yield scrapy.Request(url=book_url, meta={'item': deepcopy(item)}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']
        lis = response.xpath("//ul[@class='bk-publish clearfix']/li")
        item['author'] = lis[0].xpath("./text()").get().replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        yield item



    """
    def parse_book_list(self, response):
        item = response.meta['item']
        lis = response.xpath("//div[@id='filter-results']/ul/li")
        for li in lis:
            item['shop_name'] = li.xpath(".//div[@class='res-info']/p[@class='seller oh no-more ']/@salesname").get()
            # shop_url = li.xpath(".//div[@class='res-info']/p[@class='seller oh no-more ']/@producturl").get()
            
            # 添加https
            if 'http' not in shop_url:
                if 'www' in shop_url:
                    shop_url = 'http:' + shop_url
                else:
                    shop_url = 'https:' + shop_url

            item['shop_url'] = shop_url

            item['book_name'] = li.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/@title").get()

            book_url = li.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/@href").get()
            # 添加https
            if 'http' not in book_url:
                if 'www' in book_url:
                    book_url = 'http:' + book_url
                else:
                    book_url = 'https:' + book_url
            item['book_url'] = book_url
            
            yield item

      """


