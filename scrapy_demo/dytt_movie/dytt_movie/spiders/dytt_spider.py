# -*- coding: utf-8 -*-
import scrapy

from dytt_movie.items import DyttMovieItem


class DyttSpiderSpider(scrapy.Spider):
    name = 'dytt_spider'
    allowed_domains = ['dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/dyzz/index.html']

    # 重写父类start_requests方法
    def start_requests(self):
        reqs = []
        # 爬取（1-5页）的内容
        for i in range(1, 5):
            req = scrapy.Request('https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(i))
            reqs.append(req)
        return reqs

    def parse(self, response):
        urls = response.xpath("//a[@class='ulink']/@href").getall()
        for url in urls:
            if not url:
                return
            else:
                full_url = response.urljoin(url)
                yield scrapy.Request(full_url, callback=self.parse_detail)

    def parse_detail(self, response):
        movie_dic = DyttMovieItem()
        # 电影标题
        movie_dic["title"] = response.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()').get()
        # 在zoom内面找相应的内容（注意数组list不能使用xpath,所以取[0]）
        zoom_element = response.xpath('//div[@id="Zoom"]')[0]
        # 1获取图片
        imgs = zoom_element.xpath('.//img/@src').getall()

        if len(imgs) > 1:  # 有部分电影没有1.2电影裁图,而导致数组越界
            # 1.1海报图片
            movie_dic["poster"] = imgs[0]
            # 1.2电影裁图
            movie_dic["screen_shot"] = imgs[1]
        else:
            # 1.1海报图片
            movie_dic["poster"] = imgs[0]

        # 把div[id=Zoom]下面的span下面的所有text()获取出来
        # 下载地址
        movie_dic["download_url"] = response.xpath('.//td[@bgcolor="#fdfddf"]/a/@href').get()
        # 获取id=Zoom的div里面的所有文本
        infos = zoom_element.xpath('.//text()').getall()

        for index, info in enumerate(infos):
            if info.startswith('◎译　　名'):
                movie_dic["translated_name"] = info.replace('◎译　　名', '').strip()
            elif info.startswith('◎年　　代'):
                movie_dic["year"] = info.replace('◎年　　代', '').strip()
            elif info.startswith('◎产　　地'):
                movie_dic["country"] = info.replace('◎产　　地', '').strip()
            elif info.startswith('◎类　　别'):
                movie_dic['category'] = info.replace('◎类　　别', '').strip()
            elif info.startswith('◎语　　言'):
                movie_dic['language'] = info.replace('◎语　　言', '').strip()
            elif info.startswith('◎豆瓣评分'):
                movie_dic['douban_rating'] = info.replace('◎豆瓣评分', '').strip()
            elif info.startswith('◎片　　长'):
                movie_dic['duration'] = info.replace('◎片　　长', '').strip()
            elif info.startswith('◎导　　演'):
                movie_dic['director'] = info.replace('◎导　　演', '').strip()
            # 难点(原因：有多名主演)
            elif info.startswith('◎主　　演'):
                actor_captain = info.replace('◎主　　演', '').strip()
                # 定义一个数组
                actors_list = [actor_captain]
                # 从当前位置的下一个(index+1)开始向下找
                for x in range(index + 1, len(infos)):
                    actor = infos[x].strip()
                    # 直到出现下一下◎,结束循环
                    if actor.startswith('◎'):
                        break
                    # 加入数组列表
                    actors_list.append(actor)

                movie_dic['actors'] = actors_list

            # 简介的情况与主演员情况相似
            elif info.startswith('◎简　　介'):
                # profile_list = []
                for x in range(index + 1, len(infos)):
                    profile = infos[x].strip()
                    if profile.startswith('【下载地址】'):
                        break
                    if len(profile) > 1:
                        movie_dic['profile'] = profile
        yield movie_dic


