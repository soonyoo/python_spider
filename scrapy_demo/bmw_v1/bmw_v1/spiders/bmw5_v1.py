# -*- coding: utf-8 -*-
import scrapy

from bmw_v1.items import BmwV1Item
# scrapy.bmw_v1.bmw_v1.items.BmwV1Item


class Bmw5V1Spider(scrapy.Spider):
    name = 'bmw5_v1'
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

            item = BmwV1Item(category=category, image_urls=image_urls)
            yield item


            # print(image_urls)



            # print(image_url)
            # print(category)
            # lis = uibox.xpath(".//div[contains(@class,'uibox-con')]/ul/li/")
            # img_list = []
            # for li in lis:
            #     img = li.xpath(".//a//img/@src").get()
            #     img_list.append(img)
            # print(img_list)

