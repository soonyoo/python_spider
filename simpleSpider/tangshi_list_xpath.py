# coding = utf-8

import requests
from lxml import etree
import csv


class TangshiXpath:
    def __init__(self):
        # 思路，从简单到复杂，可先从一段代码进行分析，再到从URL直接读取
        # self.tangshi_html = "<span><a href=\"https://so.gushiwen.org/shiwenv_45c396367f59.aspx\" " \
        #                    "target=\"_blank\">行宫</a>(元稹)</span>"

        self.tangshi_list = []
        self.current_poem = dict()
        self.url = 'http://www.gushiwen.org/gushi/tangshi.aspx'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                        ' Chrome/71.0.3578.98 Safari/537.36'}

    # 从URL获取网页源码
    def get_html_from_url(self, url):
        response = requests.get(url, headers=self.headers)
        # print(response.text)
        return response.text

    # 由于遇到空值时[0] list index out of range，所以引入判断
    # 空值时返回'',否则返回list[0]
    @staticmethod
    def null_list(in_list):
        if len(in_list) < 1:
            return ''
        else:
            return in_list[0]

    # 通过xpath获取相应节点数据
    def parse_tangshi_text(self):
        # html = etree.HTML(self.tangshi_html)
        # print(html)
        # spans = html.xpath('//span')[0]
        # 注意：.//text()这样会将span下所有文本分析出来，如果./text(),则只把子文本分析出来
        # self.current_poem["author"] = spans.xpath('.//text()')
        # print(self.current_poem)

        html = etree.HTML(self.get_html_from_url(self.url))
        spans = html.xpath("//div[@class='typecont']//span")
        for span in spans:
            self.current_poem["author"] = TangshiXpath.null_list(span.xpath('./text()'))
            self.current_poem["title"] = span.xpath('./a/text()')[0]
            self.current_poem['url'] = span.xpath('./a/@href')[0]
            self.current_poem['content'] = self.parse_tangshi_content(self.current_poem['url'])
            self.tangshi_list.append(self.current_poem)
            self.current_poem = {}
        return self.tangshi_list

    # 根据url获取诗的具体内容
    def parse_tangshi_content(self, url):
        html = etree.HTML(self.get_html_from_url(url))
        tangshi_content_divs = html.xpath("//div[@class='contson']")[0].xpath('.//text()')
        return ''.join(tangshi_content_divs)

    # 保存到csv文件
    @staticmethod
    def write_2_csv(header, datas, csv_filename):
        with open(csv_filename, 'w', encoding='utf_8_sig', newline='') as fp:
            writer = csv.DictWriter(fp, header)
            writer.writeheader()
            writer.writerows(datas)


if __name__ == '__main__':
    tangshi = TangshiXpath()
    csv_header = ['author', 'title', 'url', 'content']
    csv_datas = lists = tangshi.parse_tangshi_text()
    tangshi.write_2_csv(csv_header, csv_datas, 'tangshi300.csv')

    # lists = tangshi.parse_tangshi_text()
    # for lis in lists:
    #     print(lis)
    # txt = tangshi.parse_tangshi_content('https://so.gushiwen.org/shiwenv_45c396367f59.aspx')
    # print(txt)

