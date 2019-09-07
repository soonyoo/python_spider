# -*- coding: utf-8 -*-
import scrapy
import re
from copy import deepcopy
from car_girls.items import CarGirlsItem


class BeautyGirlsSpider(scrapy.Spider):
    name = 'beauty_girls'
    allowed_domains = ['pcauto.com.cn']
    start_urls = ['https://price.pcauto.com.cn/chezhan/beauty/b24918/']

    # def start_requests(self):
    #     url = 'https://price.pcauto.com.cn/chezhan/beauty/b24918/'

    def parse(self, response):
        item = dict()
        lis = response.xpath("//ul[@id='tree']/li[@class='closeChild']")
        for li in lis:
            item['brand'] = li.xpath("./a[@class='ppLink']/em[@class='sname']/text()").get()
            item['num'] = li.xpath("./a[@class='ppLink']/span[@class='snum']/text()").get()
            javascript_function = li.xpath("./em[@class='emBox']").get()
            onclick_str = re.findall("switchSmallTypeFrame\((.*?)\)\"><i>", javascript_function)[0]
            lists = onclick_str.replace('\'', '').split(',')
            ajax_url = "https://price.pcauto.com.cn/chezhan/tree/0/{}/".format(lists[1])
            yield scrapy.Request(url=ajax_url, meta={'item': deepcopy(item)}, callback=self.parse_girls_list)

    def parse_girls_list(self, response):
        item = response.meta['item']
        lis = response.xpath("//li")
        for li in lis:
            item['title'] = li.xpath('./a/@title').get()
            url = li.xpath('./a/@href').get()
            item['url'] = response.urljoin(url)
            yield scrapy.Request(url=item['url'], meta={'item': deepcopy(item)}, callback=self.parse_girls_detail)

    def parse_girls_detail(self, response):
        item = response.meta['item']
        lis = response.xpath("//ul[contains(@class,'ulPic')]/li")
        for li in lis:
            detail_url = response.urljoin(li.xpath("./a/@href").get())
            item['detail_url'] = detail_url.replace('-1.html', '-3.html')
            yield scrapy.Request(url=item['detail_url'], meta={'item': deepcopy(item)}, callback=self.parse_girls_photo)

    def parse_girls_photo(self,response):
        item = response.meta['item']
        img_url = response.xpath("//img[@id='pic_img']/@src").get()
        item['img_url'] = response.urljoin(img_url)
        del(item['url'])
        del(item['detail_url'])
        girls_item = CarGirlsItem(brand=item['brand'],images_num=item['num'], girls_name=item['title'], image_urls=[item['img_url']])
        yield girls_item
