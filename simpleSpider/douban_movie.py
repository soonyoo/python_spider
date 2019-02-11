# coding = utf-8

import requests
from lxml import etree

"""
爬取豆瓣电影内容【正在上映】
https://movie.douban.com/cinema/nowplaying/guangzhou/
技术选型：requests, xpath
"""


class DouBanMovie:
    def __init__(self):
        self.movie_list = []
        self.now_play_info = {}
        self.url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
        self.headers = {'referer': 'https://movie.douban.com/cinema/nowplaying/shaoyang/',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    # 获取html源码
    def get_html_from_url(self):
        response = requests.get(self.url, headers=self.headers)
        # print(response.text)
        return response.text

    # 通过xpath获取网页源码相应节点数据
    def parse_douban(self):
        html = etree.HTML(self.get_html_from_url())
        # print(html)
        ul = html.xpath('//ul[@class="lists"]')[0]
        # print(ul)
        lis = ul.xpath('./li')
        for li in lis:
            self.now_play_info['title'] = li.xpath('@data-title')[0]
            self.now_play_info['score'] = li.xpath('@data-score')[0]
            self.now_play_info['release'] = li.xpath('@data-release')[0]
            self.now_play_info['duration'] = li.xpath('@data-duration')[0]
            self.now_play_info['region'] = li.xpath('@data-region')[0]
            self.now_play_info['director'] = li.xpath('@data-director')[0]
            self.now_play_info['actors'] = li.xpath('@data-actors')[0]
            self.now_play_info['img'] = li.xpath('.//img/@src')[0]
            self.movie_list.append(self.now_play_info)
            self.now_play_info = {}
        return self.movie_list


if __name__ == '__main__':
    douban = DouBanMovie()
    movie_list = douban.parse_douban()
    for movie in movie_list:
        print(movie)

