# coding = utf-8

import json


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


if __name__ == '__main__':
    # test = Test()
    # test.shu_zhu_dict()
    # test.do_mp4_str()
    # test.index_test()
    Test.list_cut()




    # # print(str1.find('='))
    # url = str1[34:]
    #
    # full_path ='http://content.wsxy.chinaunicom.com'+url
    # print(full_path)

    # test = Test()

