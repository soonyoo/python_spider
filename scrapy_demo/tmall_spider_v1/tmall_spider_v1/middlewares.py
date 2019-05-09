# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver_path = r'D:\python\chromedriver\chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path=self.driver_path)

    def process_request(self, request, spider):
        self.browser.get(request.url)
        time.sleep(3)
        source = self.browser.page_source
        # print(source)
        response = HtmlResponse(url=self.browser.current_url, body=source, request=request, encoding='utf-8')
        return response
