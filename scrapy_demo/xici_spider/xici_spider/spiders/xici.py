# -*- coding: utf-8 -*-
import scrapy

from xici_spider.items import XiciSpiderItem
import re


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1']

    # 初始request
    def start_requests(self):
        reqs = []
        for i in range(1, 3):
            req = scrapy.Request('https://www.xicidaili.com/nn/{}'.format(i))
            reqs.append(req)
        return reqs

    def parse(self, response):
        # 跳过第一行，字段行
        trs = response.xpath("//table[@id='ip_list']/tr")[1:]

        # 定义返回值
        # yield 回去的必须为字典dict;List试过不行。
        for tr in trs:
            item = XiciSpiderItem()
            tds = tr.xpath("./td")
            # ip
            item['ip'] = tds[1].xpath("./text()").get()
            # 端口
            item['port'] = tds[2].xpath("./text()").get()
            # 位置
            item['position'] = tds[3].xpath("./a/text()").get()
            # 类型
            item['type'] = tds[5].xpath("./text()").get()
            # 速度speed内容为：0.803秒
            # 使用正则表达式: 0.803秒 ==> 0.803 (去掉中文内容)
            speed_string = tds[6].xpath("./div/@title").get()
            item['speed'] = re.findall(r"\d+\.\d+", speed_string)[0]
            # 验证时间
            item['last_check_time'] = tds[-1].xpath("./text()").get()
            yield item
        """
        写法一（旧）：
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
        """




