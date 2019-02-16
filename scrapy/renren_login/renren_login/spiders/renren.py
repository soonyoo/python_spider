# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {'email': '18688280440', 'password': '****'}
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self,response):
        url = "http://www.renren.com/969741257/profile"
        request = scrapy.Request(url, callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open('dh.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)





