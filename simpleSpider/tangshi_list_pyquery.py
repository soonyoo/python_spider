# coding=utf-8
import re
from pyquery import PyQuery as pQ
"""
 从古诗文网中爬取[唐诗三百首]
 使用技术：正则表达式、pyQuery 
"""


class PoemParser:
    def __init__(self):
        self.tangshi_list = []
        self.current_poem = {}

    # 从URL中解析html源码
    @staticmethod
    def get_html_from_url(url):
        doc = pQ(url=url, encoding="utf-8")  # 增加encoding="utf-8"，防止中文乱码
        return doc

    # 从古诗文网中爬取[唐诗三百首]
    def get_tangshi_list(self):
        doc = PoemParser.get_html_from_url('http://www.gushiwen.org/gushi/tangshi.aspx')
        spans = doc('span').items()  # .items()方法，返回一个迭代对象。class 'generator'
        for span in spans:
            # 解析出作者
            author = re.search('</a>(.*?)</span>', str(span)).group(1)
            self.current_poem["author"] = author.replace('(', '').replace(')', '')  # 替换()
            # 1解析a标签
            a_tag = span('span a')
            # 1.1 解析出标题
            self.current_poem["title"] = a_tag.text()
            # 1.2 解析出标题
            self.current_poem["url"] = a_tag.attr.href
            # 加入数组
            self.tangshi_list.append(self.current_poem)
            # 清空对象，进入下次循环赋值
            self.current_poem = {}
        return self.tangshi_list


if __name__ == '__main__':
    parser = PoemParser()
    lists = parser.get_tangshi_list()
    for i in range(len(lists)):
        print('标题: %(title)s\t作者：%(author)s\tURL: %(url)s' % (lists[i]))
