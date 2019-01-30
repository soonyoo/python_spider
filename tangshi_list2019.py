# -*- coding: utf-8 -*-
import requests
import re
# from HTMLParser import HTMLParser
from html.parser import HTMLParser


def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None


class PoemParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        # self.in_div = False
        self.in_span = False
        self.in_a = False

        self.pattern = re.compile(r'(.*)\((.*)\)')
        self.tangshi_list = []
        self.current_poem = {}

    def handle_starttag(self, tag, attrs):

        #span标签
        if tag == 'span':
            self.in_span = True

        # 在span里面，并且是a标签
        if tag == 'a' and self.in_span:
            self.in_a = True
            self.current_poem['url'] = _attr(attrs, 'href')

    def handle_endtag(self, tag):
        if tag == 'span':
            self.in_span = False
        #
        # if tag == 'a':
        #     self.in_a = False

    def handle_data(self, data):
        if self.in_a:
            print(data)
            m = self.pattern.match(data)
            if m:
                self.current_poem['title'] = m.group(1)
                self.current_poem['author'] = m.group(2)
                self.tangshi_list.append(self.current_poem)
                self.current_poem = {}

def retrive_tangshi_300():
    url = 'http://www.gushiwen.org/gushi/tangshi.aspx'
    r = requests.get(url)
    parser = PoemParser()
    parser.feed(r.content.decode('utf-8'))

    # print(parser.handle_data(data))
    return parser.tangshi_list
    # print(r.content.decode('utf-8'))

if __name__ == '__main__':
    l = retrive_tangshi_300()
     # print(l)
    # retrive_tangshi_300()
    print('total %d poems.' % len(l))
    for i in range(10):
        print('标题: %(title)s\t作者：%(author)s\tURL: %(url)s' % (l[i]))