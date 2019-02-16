# -*- coding: utf-8 -*-
import scrapy
from bmw_v2.items import BmwV2Item

class Bmw5V2Spider(scrapy.Spider):
    name = 'bmw5_v2'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()
            image_urls = uibox.xpath('.//ul/li/a/img/@src').getall()

            # for image_url in image_urls:
            #     url = response.urljoin(image_url)
            #     print(url)

            image_urls = list(map(lambda image_url: response.urljoin(image_url), image_urls))

            item = BmwV2Item(category=category, image_urls=image_urls)
            yield item