# -*- coding: utf-8 -*-
import scrapy

from xici_spider.items import XiciSpiderItem
import re


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1']

    def start_requests(self):
        reqs = []
        for i in range(11):
            req = scrapy.Request('https://www.xicidaili.com/nn/{}'.format(i))
            reqs.append(req)
        return reqs

    def parse(self, response):
        # 跳过第一行，字段行
        trs = response.xpath("//table[@id='ip_list']/tr")[1:]
        for tr in trs:
            tds = tr.xpath("./td")
            ip = tds[1].xpath("./text()").get()
            port = tds[2].xpath("./text()").get()
            position = tds[3].xpath("./a/text()").get()
            type = tds[5].xpath("./text()").get()
            speed = tds[6].xpath("./div/@title").get()
            # 使用正则表达式，0.803秒 ==> 0.803 (去掉中文内容)
            speed = re.findall(r"\d+\.\d+", speed)[0]
            last_check_time = tds[-1].xpath("./text()").get()
            item = XiciSpiderItem(ip=ip, port=port, position=position, type=type, speed=speed, last_check_time=last_check_time)
            yield item
            # print(item)
            # break
            # print(ip)
            # break




