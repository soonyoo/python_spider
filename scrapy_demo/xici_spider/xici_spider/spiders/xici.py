# -*- coding: utf-8 -*-
import scrapy

from xici_spider.items import XiciSpiderItem
import re


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1']

    def parse(self, response):
        # print('进来了。。。。')
        trs = response.xpath("//table[@id='ip_list']/tr")[1:]
        # print(type(trs))
        # print(len(trs))
        for tr in trs:
            tds = tr.xpath("./td")
            ip = tds[1].xpath("./text()").get()
            port = tds[2].xpath("./text()").get()
            position = tds[3].xpath("./a/text()").get()
            type = tds[5].xpath("./text()").get()
            speed = tds[6].xpath("./div/@title").get()
            speed = re.findall(r"\d+\.\d+", speed)[0]
            last_check_time = tds[-1].xpath("./text()").get()
            item = XiciSpiderItem(ip=ip, port=port, position=position, type=type, speed=speed, last_check_time=last_check_time)
            yield item
            # print(item)
            # break
            # print(ip)
            # break




