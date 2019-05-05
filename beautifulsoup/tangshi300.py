# coding = utf-8

from bs4 import BeautifulSoup
import requests
# import re


class Tangshi(object):
    def __init__(self):
        self.tangshi_list = []
        self.current_poem = dict()
        self.url = 'http://www.gushiwen.org/gushi/tangshi.aspx'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/71.0.3578.98 Safari/537.36'}

    def parser(self):
        response = requests.get(self.url, headers=self.headers)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        # 1.获取所有class="typecont" 的div
        divs = soup.find_all('div', attrs={'class': 'typecont'})
        for div in divs:
            book_mark = div.find('div', attrs={'class': 'bookMl'}).string
            spans = div.find_all('span')
            for span in spans:
                self.current_poem["book_mark"] = book_mark
                self.current_poem["title"] = span.find('a').text
                self.current_poem["author"] = str(span.find('a').next_sibling).replace('(', '').replace(')', '')
                self.current_poem['url'] = span.find('a').attrs['href']
                self.tangshi_list.append(self.current_poem)
                self.current_poem = {}
        return self.tangshi_list


if __name__ == '__main__':
    tangshi = Tangshi()
    tangshi_lis = tangshi.parser()
    for lis in tangshi_lis:
        print(lis)







