# coding: utf-8

from lxml import etree
import requests
import pymysql
import uuid


class NeteasyRank(object):
    def __init__(self):
        self.url = 'http://news.163.com/rank/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                        ' Chrome/71.0.3578.98 Safari/537.36'}
        self.news = dict()
        self.news_list = []

        db_params = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'QAZ123qaz#',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**db_params)
        self.cursor = self.conn.cursor()
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into news163(id,title_id,url,type,title,click_num) values (%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql

    def parse(self):
        response = requests.get(self.url, headers=self.headers)
        # response.encoding = 'utf-8'
        content = response.text
        html = etree.HTML(content)

        lis = html.xpath("//div[@id='whole']/following-sibling::div[1]/div[@class='tabBox']/div[@class='title-tab']/ul/li")
        tab_contents = html.xpath("//div[@id='whole']/following-sibling::div[1]/div[@class='tabBox']/div[contains(@class,'tabContents')]")

        for i, li in enumerate(lis):
            tab_text = li.xpath('./text()')[0]
            trs = tab_contents[i].xpath('.//tr')[1:]
            for tr in trs:
                tds = tr.xpath("./td")
                self.news['type'] = tab_text
                self.news['id'] = str(uuid.uuid1())
                self.news['title_id'] = tds[0].xpath('./span/text()')[0]
                self.news['url'] = tds[0].xpath('./a/@href')[0]
                self.news['title'] = tds[0].xpath('./a/text()')[0]
                self.news['click_num'] = tds[1].xpath('./text()')[0]
                ###################
                #                             id,url,type,title,click_num) values (%s,%s,%s,%s,%s)
                #
                self.cursor.execute(self.sql, (self.news['id'], self.news['title_id'], self.news['url'],
                                               self.news['type'], self.news['title'],
                                               self.news['click_num'])
                                    )

                self.conn.commit()

                self.news_list.append(self.news)
                self.news = {}

        return self.news_list


if __name__ == '__main__':
    net163 = NeteasyRank()
    list_news = net163.parse()
    print(net163.sql)

    for new in list_news:

        print(new)

