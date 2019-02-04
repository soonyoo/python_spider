# coding = utf-8

from lxml import etree


class TangshiXpath:
    def __init__(self):
        self.tangshi_html = "<span><a href=\"https://so.gushiwen.org/shiwenv_45c396367f59.aspx\" target=\"_blank\">行宫</a>(元稹)</span>"
        self.tangshi_list = []
        self.current_poem = {}

    def tangshi_text(self):
        html = etree.HTML(self.tangshi_html)
        self.current_poem["author"] = html.xpath('//span/text()')[0]
        self.current_poem["title"] = html.xpath('//span/a/text()')[0]
        self.current_poem['url'] = html.xpath('//span/a/@href')[0]
        self.tangshi_list.append(self.current_poem)
        self.current_poem = {}
        return self.tangshi_list


if __name__ == '__main__':
    tangshi = TangshiXpath()
    lists = tangshi.tangshi_text()
    print(lists)
