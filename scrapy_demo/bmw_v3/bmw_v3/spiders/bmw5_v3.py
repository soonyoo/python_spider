# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bmw_v3.items import BmwV3Item


class Bmw5V3Spider(CrawlSpider):
    name = 'bmw5_v3'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        category = response.xpath("//div[@class='uibox']/div[@class='uibox-title']/text()").get()
        srcs = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()

        # srcs = list(map(lambda x: x.replace("t_",""),srcs))
        ## urls = []
        ## for src in srcs:
        ##     url = response.urljoin(src)
        ##     urls.append(url)
        # srcs = list(map(lambda x: response.urljoin(x), srcs))
        #以上代码可用一行来完成
        srcs = list(map(lambda x: response.urljoin(x.replace("t_", "")), srcs))
        yield BmwV3Item(category=category,image_urls=srcs)




