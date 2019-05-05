# -*- coding: utf-8 -*-

from html.parser import HTMLParser
import re


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_div = False
        self.in_span = False
        self.in_a = False
        # self.pattern = re.compile(r'(.*)\((.*)\)')
        self.pattern = re.compile(r'\((.*)\)')
        self.current_poem = {}
        self.tangshi_list = []

    def _attr(self, attrs, attrname):
        for attr in attrs:
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        if tag == 'a':
            self.in_a = True
            self.current_poem['url'] = self._attr(attrs, 'href')
            # print(attrs)
            # self.current_poem['title'] = re.findall('',)

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        print(data)
        m = self.pattern.match(data)
        if m:
            # self.current_poem['title'] = m.group()
            self.current_poem['author'] = m.group()
            self.tangshi_list.append(self.current_poem)
            self.current_poem = {}

def retrive_tangshi_300():
    # html = "<a href=\"https://so.gushiwen.org/shiwenv_45c396367f59.aspx\" target=\"_blank\">行宫(元稹)</a>"
    html = "<a href=\"https://so.gushiwen.org/shiwenv_45c396367f59.aspx\" target=\"_blank\">行宫</a>(元稹)"
    # parser = MyHTMLParser()
    # parser.feed(html)
    current_poem = {}
    list1 = re.findall(r'">(.*?)</a>\((.*)\)', html)
    # <a href="(.*?)"
    current_poem['title'] = list1[0][0]
    current_poem['author'] = list1[0][1]
    print(current_poem)


if __name__ == '__main__':
    retrive_tangshi_300()
    # print('total %d poems.' % len(l))
    # print('标题: %(title)s\t作者：%(author)s\tURL: %(url)s' % (l[0]))
    # html = "行宫\n(元稹)"
    # print(html)



