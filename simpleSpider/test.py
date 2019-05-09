# coding = utf-8

import json
import time

import uuid
from lxml import etree


class Test(object):
    def __init__(self):
        print('from init')

    def do_something(self):
        print('do something...')

    def shu_zhu_dict(self):
        json_str = '{"size":50,"number":0,"totalElements":43,"last":true,"totalPages":1,"sort":null,"first":true,"numberOfElements":43,"content":"aa"}'
        dictinfo = json.loads(json_str)
        print(type(dir(dictinfo)))
        content = dictinfo["content"]
        print(content)

    def do_string(self):
        str1 = 'http://wsxy.chinaunicom.cn/learner/play/course/%s;classroomId=49651475;courseDetailId=%s;' % ('49143893','123456')
        print(str1)

    # 查找MP4位置
    def do_mp4_str(self):
        str1 = '/lmsapi/video/cmi-ck.html?content=/content/content_server/11392008/2017/0930105145413/30013.mp4&sources=%5B%7B%22label%22%3A%22%E5%8E%9F%E7%94%BB%22%2C%22file%22%3A%22%2Fcontent%2Fupload%2F2019%2F01%2F28%2F5f41e81b-19c4-4287-aa55-5c48e61f6e9b-866.mp4'
        begin_url = str1.find('=/content')
        end_url = str1.find('.mp4')
        url = str1[begin_url+1:end_url+4]
        full_path = 'http://content.wsxy.chinaunicom.com' + url
        print(full_path)

    def index_test(self):
        str1 = '/lmsapi/video/cmi-ck.html?content=/content/content_server/11392008/2017/0930105145413/30013.mp4&sources=%5B%7B%22label%22%3A%22%E5%8E%9F%E7%94%BB%22%2C%22file%22%3A%22%2Fcontent%2Fupload%2F2019%2F01%2F28%2F5f41e81b-19c4-4287-aa55-5c48e61f6e9b-866.mp4'
        begin_url = str1.index('=/content')
        end_url = str1.index('.mp4')
        print(begin_url)
        print(end_url)
        url = str1[begin_url+1:end_url+4]
        full_path = 'http://content.wsxy.chinaunicom.com' + url
        print(full_path)

    @staticmethod
    def list_cut():
        lis = ['a', 'b', 'c', 'd']
        lis1 = lis[1:]
        print(lis1)

    @staticmethod
    def url_split():
        url1 = 'https://www.jianshu.com/p/9cd222f65efa?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation'
        url2 = 'https://www.jianshu.com/p/f9fb7ea4bf32'
        # url_show = url1.split('?')[0]
        url_show = url2.split('?')[0]
        return url_show

    @staticmethod
    def start_req():
        reqs = []
        for i in range(11):
            req = 'https://www.xicidaili.com/nn/{}'.format(i)
            reqs.append(req)
        return reqs


# 两种不同url
# https://www.jianshu.com/p/9cd222f65efa?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
# https://www.jianshu.com/p/f9fb7ea4bf32


if __name__ == '__main__':
    list1 = Test.start_req()
    for lis in list1:
        print(lis)
    # url = Test.url_split()
    # print(url)
    # t = "2017-11-24 17:30:00"
    # pub_time = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    # print(type(pub_time))
    # print(pub_time.ctime)
    # print(type(t.time))

    # print(uuid.uuid1())
    # print(type(str(uuid.uuid1())))
    # html = """
    # <span class="views-count">阅读 22987</span>
    # """
    # html = etree.HTML(html)
    # span_text = html.xpath("//span[@class='views-count']/text()")[0].split(' ')[-1]
    # print(span_text)

    # 将其转换为时间数组
    # time_struct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    # print()


    # for x in range(1, 3):
    #     print(x)
    # test = Test()
    # test.shu_zhu_dict()
    # test.do_mp4_str()
    # test.index_test()
    # Test.list_cut()




    # # print(str1.find('='))
    # url = str1[34:]
    #
    # full_path ='http://content.wsxy.chinaunicom.com'+url
    # print(full_path)

    # test = Test()

    html = """
    <span style="color: rgb(0, 51, 51); size: 2px; text-decoration: none; cursor: pointer;" 
    onmouseover="this.style.color=&quot;#ff3333&quot;" 
    onmouseout="this.style.color=&quot;#003333&quot;" 
    onclick="window.open(&quot;/jsp/cnceb/web/info1/detailNotice.jsp?id=2875703300000014418&quot;,&quot;&quot;,&quot;
    height=600,width=900,left=60,toolbar=yes,
    menubar=yes,scrollbars=yes,resizable=yes,status=yes&quot;);"
    title="2019年中国联通广东湛江LTEFDD室分口碑场景新建一期工程湛江工程项目直放站采购项目(第二次）竞争性谈判公告">2019年中国联通广东湛江LTEFDD室分口碑场景新建一期工程湛江工程...
									
									</span>
    """
    # html = etree.HTML(html)
    # span = html.xpath('//span')[0]
    # span_title = span.xpath("@title")[0]
    # span_onclick = span.xpath("@onclick")[0]
    # print(span_onclick)

    # onclick_start = span_onclick.find('\"')
    # print(onclick_start)

    # onclick_end = span_onclick.find('\"', onclick_start+1)
    # print(onclick_end)
    # print(span_onclick[onclick_start+1:onclick_end])


    # span_onclick_url = span_onclick.find('\"', 13)
    # print(span_onclick)
    # print(span_onclick_url)
    # print(span_onclick[13:73])


