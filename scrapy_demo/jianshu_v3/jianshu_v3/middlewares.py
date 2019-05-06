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
        # self.driver = webdriver.chrome(executable_path=r'D:\python\chromedriver\chromedriver.exe')

    def process_request(self, request, spider):
        self.browser.get(request.url)
        time.sleep(1)
        # 点击[展开更多] > (如果有，一直点下去。。。)
        try:
            while True:
                show_more = self.browser.find_elements_by_class_name('show-more')
                show_more.click()
                time.sleep(0.3)
                if not show_more:
                    break
        except:
            pass

        source = self.browser.page_source
        response = HtmlResponse(url=self.browser.current_url, body=source, request=request, encoding='utf-8')
        return response

