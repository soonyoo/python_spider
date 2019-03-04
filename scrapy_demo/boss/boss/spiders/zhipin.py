# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100/?query=python&page=1']
    # 匹配职位列表页的规则
    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
    )

    rules = (
        Rule(LinkExtractor(allow=r'.+job_detail/.+\.html'), callback="parse_job", follow=False),
    )

    def parse_job(self, response):
        # xpath语法，提取网页信息
        name = response.xpath("//div[@class='name']/h1/text()").get()
        name = name.strip() if name else '无'

        salary = response.xpath("//span[@class='salary']/text()").get()
        salary = salary.strip() if salary else '无'

        job_info = response.xpath('//div[contains(@class, "job-primary ")]/div[@class="info-primary"]/p//text()').getall()
        if job_info:
            city = job_info[0]
            work_years = job_info[1]
            education = job_info[2]
        else:
            city = '无'
            work_years = '无'
            education = '无'
        company = response.xpath("//div[@class='info-company']//a/text()").get()
        company = company.strip() if company else '无'
        yield BossItem(name=name, salary=salary, city=city, work_years=work_years, education=education,
                              company=company)
