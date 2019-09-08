# -*- coding: utf-8 -*-
import scrapy
from filesPipeline_demo.items import FilespipelineDemoItem



class TwistedSpider(scrapy.Spider):
    name = 'twisted'
    allowed_domains = ['twistedmatrix.com']
    start_urls = ['https://twistedmatrix.com/documents/current/core/examples/']

    def parse(self, response):
        urls = response.xpath("//a[@class='reference download internal']/@href").getall()
        titles = response.xpath("//a[@class='reference download internal']/code/span/text()").getall()

        for url,title in zip(urls,titles):
            yield FilespipelineDemoItem(file_urls=[response.urljoin(url)],file_name=title)


        # item_urls = []
        # for url in urls:
        #
        #     item_urls.append(response.urljoin(url))
        # yield FilespipelineDemoItem(file_urls=item_urls)
