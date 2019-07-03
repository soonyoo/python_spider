# coding = utf-8

import requests
from lxml import etree


class DyttMovieParse:
    def __init__(self):
        self.movie_list = []
        self.movie_dic = {}
        self.movie_url = 'https://www.dytt8.net/html/gndy/dyzz/index.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/71.0.3578.98 Safari/537.36'}
        self.BASE_URL = 'https://www.dytt8.net'
        self.URL_LIST = []

    # 从URL获取网页源码
    def get_html_from_url(self, url, charset):
        response = requests.get(url, headers=self.headers)
        response.encoding = charset
        html = response.text
        return html
        # print(html)
        # print(response.encoding)
        # print(response.text)
        # return response.text

    def get_movie_url_list(self, outside_url):
        html = etree.HTML(self.get_html_from_url(outside_url, 'GBK'))
        urls = html.xpath('//a[@class="ulink"]/@href')
        for url in urls:
            self.URL_LIST.append(self.BASE_URL+url)
        return self.URL_LIST

    def parse_dytt_movie(self, detail_url):
        # url = 'https://www.dytt8.net/html/gndy/dyzz/20190131/58131.html'
        html = etree.HTML(self.get_html_from_url(detail_url, 'GBK'))

        # 电影标题
        self.movie_dic["title"] = html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
        # 在zoom内面找相应的内容（注意数组list不能使用xpath,所以取[0]）
        zoom_element = html.xpath('//div[@id="Zoom"]')[0]
        # 1获取图片
        imgs = zoom_element.xpath('.//img/@src')
        # 1.1海报图片
        self.movie_dic["poster"] = imgs[0]
        # 1.2电影裁图
        self.movie_dic["screen_shot"] = imgs[1]
        # 把div[id=Zoom]下面的span下面的所有text()获取出来
        # 下载地址
        self.movie_dic["download_url"] = html.xpath('.//td[@bgcolor="#fdfddf"]/a/@href')[0]
        # 获取id=Zoom的div里面的所有文本
        infos = zoom_element.xpath('.//text()')
        for index, info in enumerate(infos):
            # print(index)
            # print('==')
            # print(info)
            if info.startswith('◎译　　名'):
                self.movie_dic["translated_name"] = info.replace('◎译　　名', '').strip()
            elif info.startswith('◎年　　代'):
                self.movie_dic["year"] = info.replace('◎年　　代', '').strip()
            elif info.startswith('◎产　　地'):
                self.movie_dic["country"] = info.replace('◎产　　地', '').strip()
            elif info.startswith('◎类　　别'):
                self.movie_dic['category'] = info.replace('◎类　　别', '').strip()
            elif info.startswith('◎语　　言'):
                self.movie_dic['language'] = info.replace('◎语　　言', '').strip()
            elif info.startswith('◎豆瓣评分'):
                self.movie_dic['douban_rating'] = info.replace('◎豆瓣评分', '').strip()
            elif info.startswith('◎片　　长'):
                self.movie_dic['duration'] = info.replace('◎片　　长', '').strip()
            elif info.startswith('◎导　　演'):
                self.movie_dic['director'] = info.replace('◎导　　演', '').strip()
            # 难点(原因：有多名主演)
            elif info.startswith('◎主　　演'):
                actor_captain = info.replace('◎主　　演', '').strip()
                # 定义一个数组
                actors_list = [actor_captain]
                # 从当前位置的下一个(index+1)开始向下找
                for x in range(index+1, len(infos)):
                    actor = infos[x].strip()
                    # 直到出现下一下◎,结束循环
                    if actor.startswith('◎'):
                        break
                    # 加入数组列表
                    actors_list.append(actor)

                self.movie_dic['actors'] = actors_list

            # 简介的情况与主演员情况相似
            elif info.startswith('◎简　　介'):
                # profile_list = []
                for x in range(index + 1, len(infos)):
                    profile = infos[x].strip()
                    if profile.startswith('【下载地址】'):
                        break
                    if len(profile) > 1:
                        self.movie_dic['profile'] = profile
        return self.movie_dic

    def spider(self):
        base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        for x in range(1, 3):
            outside_url = base_url.format(x)
            detail_urls = self.get_movie_url_list(outside_url)
            for detail_url in detail_urls:
                self.movie_list.append(self.parse_dytt_movie(detail_url))
                self.movie_dic = {}
        return self.movie_list


if __name__ == '__main__':
    dytt = DyttMovieParse()
    # dytt.get_html_from_url()
    # lists = dytt.get_movie_url_list()
    # dytt.parse_dytt_movie(lists[0])
    # for list in lists:
    #     print(list)
    # dytt.parse_dytt_movie()
    lists = dytt.spider()
    for list in lists:
        print(list)


