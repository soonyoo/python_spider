# coding = utf-8
import requests
from lxml import etree
# from lxml.html import fromstring, tostring
import pymysql


class ChinaUincom(object):
    def __init__(self):
        # self.url = 'http://gd.chinaunicombidding.cn/jsp/cnceb/web/forword.jsp'
        self.url = 'http://gd.chinaunicombidding.cn/jsp/cnceb/web/info1/infoList.jsp'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/71.0.3578.98 Safari/537.36'}

        self.base_url = 'http://gd.chinaunicombidding.cn'
        self.biao_dict = dict()
        self.biao_list = []

        db_params = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'QAZ123qaz#',
            'database': 'biao',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**db_params)
        self.cursor = self.conn.cursor()
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into biao_info(title,pub_date,city) values (%s,%s,%s)
                """
            return self._sql
        return self._sql

    def parse(self):
        response = requests.get(self.url, headers=self.headers)
        # html_text = response.text
        # print(html_text)

        html = etree.HTML(response.text)
        # trs = html.xpath("//div[@id='div1']")
        # print(trs)

        trs = html.xpath("//div[@id='div1']/table/tr")
        for tr in trs:
            tds = tr.xpath('./td')
            span = tds[0].xpath('./span')[0]
            self.biao_dict["title"] = span.xpath("@title")[0]
            self.biao_dict["pub_date"] = tds[1].xpath('./text()')[0]
            self.biao_dict["city"] = tds[2].xpath('@title')[0]
            self.biao_list.append(self.biao_dict)
            self.biao_dict = {}
        # print(self.biao_list)
        return self.biao_list

    def get_data(self, start_page, end_page):
        """
        根据输入的页数，爬取相应的内容
        :param start_page:
        :param end_page:
        :return:
        """
        base_url = 'http://gd.chinaunicombidding.cn/jsp/cnceb/web/info1/infoList.jsp?page={}'
        for x in range(start_page, end_page):
            outside_url = base_url.format(x)
            response = requests.get(outside_url, headers=self.headers)
            html = etree.HTML(response.text)
            trs = html.xpath("//div[@id='div1']/table/tr")
            for tr in trs:
                tds = tr.xpath('./td')
                span = tds[0].xpath('./span')[0]
                self.biao_dict["title"] = span.xpath("@title")[0]
                self.biao_dict["pub_date"] = tds[1].xpath('./text()')[0]
                self.biao_dict["city"] = tds[2].xpath('@title')[0]
                # 获取url
                urls = span.xpath("@onclick")[0]
                urls_s = urls.find('\"')
                urls_e = urls.find('\"', urls_s + 1)
                url = urls[urls_s+1:urls_e]
                full_url = self.base_url + url
                self.biao_dict["content_url"] = full_url
                # content_dict = self.parse_detail(full_url)
                # self.biao_dict["s_id"] = self.parse_detail(full_url)
                # self.biao_dict["content"] = content_dict["content"]
                self.biao_list.append(self.biao_dict)
                # 入库mysql
                # self.cursor.execute(self.sql, (self.biao_dict["title"], self.biao_dict["pub_date"], self.biao_dict["city"]))

                self.biao_dict = {}
            # 每页内容入commit一次
            # self.conn.commit()
        # print('###成功####')
        return self.biao_list

    def parse_detail(self, url):
        """
        获取每个标里面的内容
        :param url:
        :return:
        """
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.text)
        serial_number = html.xpath("//td[@class='MsoNormal']/span/text()")[0].replace('\n', '').replace('\r', '').replace(' ', '').split('：')[-1]
        content_html = html.xpath("/html/body/div/p[2]")[0]
        result = etree.tostring(content_html, encoding='utf-8', method="xml", pretty_print=True)
        content = result.decode("utf-8")
        content_dict = {"s_id": serial_number, "content": content}
        return content_dict


if __name__ == '__main__':
    chinaUincom = ChinaUincom()
    chinaUincom.get_data(1, 20)
    # 只分析一页
    # biao_list = chinaUincom.parse()
    # for biao in biao_list:
    #     print(biao)
    # 多页分析
    biao_list = chinaUincom.get_data(1, 3)
    for biao in biao_list:
        print(biao)

    # dict1 = chinaUincom.parse_detail('http://gd.chinaunicombidding.cn/jsp/cnceb/web/info1/detailNotice.jsp?id=2863703300000014997')
    # print(dict1)

    # chinaUincom.parse_detail('http://gd.chinaunicombidding.cn/jsp/cnceb/web/info1/detailNotice.jsp?id=2863703300000014997')









