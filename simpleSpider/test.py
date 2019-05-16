# coding = utf-8

import json
import time

import uuid
from lxml import etree
from bs4 import BeautifulSoup

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

    @staticmethod
    def get_html():
        html = """
        <html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{"size":50,"number":0,"totalElements":43,"last":true,"totalPages":1,"sort":null,"first":true,"numberOfElements":43,"content":[{"id":49143893,"name":"天宫平台技术培训13-资源申请流程","sourceCourseId":21460624,"description":null,"code":"20190130_000589","duration":18,"period":0.4,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189151624.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3232,"likes":299,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36680,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143892,"name":"天宫平台技术培训12-平台租户资源分配","sourceCourseId":21460626,"description":null,"code":"20190130_000588","duration":5,"period":0.11,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189119040.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3121,"likes":297,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36679,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143891,"name":"天宫平台技术培训11-负载均衡","sourceCourseId":21460628,"description":null,"code":"20190130_000587","duration":3,"period":0.07,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189160207.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3161,"likes":309,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36678,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143890,"name":"天宫平台技术培训10-分布式应用服务排错","sourceCourseId":21460630,"description":null,"code":"20190130_000586","duration":11,"period":0.24,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189144230.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3241,"likes":274,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36677,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143889,"name":"天宫平台技术培训09-分布式应用服务开发环境搭建","sourceCourseId":21460632,"description":null,"code":"20190130_000585","duration":4,"period":0.09,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189179471.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3253,"likes":273,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36676,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143888,"name":"天宫平台技术培训08-分布式应用服务开发常见问题","sourceCourseId":21460634,"description":null,"code":"20190130_000584","duration":7,"period":0.16,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189129458.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3236,"likes":286,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36675,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143887,"name":"天宫平台技术培训07-分布式应用服务界面使用","sourceCourseId":21460636,"description":null,"code":"20190130_000583","duration":9,"period":0.2,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189084346.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3397,"likes":298,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36674,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143886,"name":"天宫平台技术培训06-分布式消息控制台","sourceCourseId":21460638,"description":null,"code":"20190130_000582","duration":6,"period":0.13,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189027249.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3280,"likes":283,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36673,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143885,"name":"天宫平台技术培训05-分布式消息开发","sourceCourseId":21460640,"description":null,"code":"20190130_000581","duration":6,"period":0.13,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189109399.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3318,"likes":262,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36672,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143884,"name":"天宫平台技术培训04-分布式搜索引擎视频","sourceCourseId":21460642,"description":null,"code":"20190130_000580","duration":14,"period":0.31,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189103532.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3351,"likes":276,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36671,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143883,"name":"天宫平台技术培训03-分布式数据库服务","sourceCourseId":21460644,"description":null,"code":"20190130_000579","duration":25,"period":0.56,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189097624.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3539,"likes":289,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36670,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143882,"name":"天宫平台技术培训02-分布式缓存服务","sourceCourseId":21460646,"description":null,"code":"20190130_000578","duration":3,"period":0.07,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189064098.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":3628,"likes":272,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36669,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143881,"name":"天宫平台技术培训01-分布式对象存储服务","sourceCourseId":21460648,"description":null,"code":"20190130_000577","duration":13,"period":0.29,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189058610.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":4194,"likes":299,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36668,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143880,"name":"天宫平台技术培训14-java代码规约插件教程","sourceCourseId":21471656,"description":null,"code":"20190130_000576","duration":14,"period":0.31,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/public/portall/1479189203613.jpg","categoryId":32064824,"categoryName":"企业信息化","point":null,"learners":2974,"likes":242,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36667,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143846,"name":"天宫平台技术培训-cDMS使用视频-用户使用","sourceCourseId":49143846,"description":null,"code":"20190128_000541","duration":14,"period":0.31,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2019/01/28/b1fa37b1-aeda-442e-a859-63b01220c5c4.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":508,"likes":112,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36633,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143845,"name":"天宫平台技术培训-cDMS使用视频-DBA系统设置","sourceCourseId":49143845,"description":null,"code":"20190128_000540","duration":10,"period":0.22,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2019/01/28/6997401c-d127-44f6-939b-2d0026c139b8.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":487,"likes":111,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36632,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143334,"name":"中国联通IT能力商店","sourceCourseId":49143321,"description":null,"code":"20181228_000116","duration":47,"period":1.04,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/12/28/1b2f2b51-b7ef-428c-9212-51b4e967be5a.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2517,"likes":394,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36121,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143333,"name":"一体化能力开放体系总体介绍","sourceCourseId":49143322,"description":null,"code":"20181228_000115","duration":56,"period":1.24,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/12/28/9c601837-0511-4cf9-8480-a7e612e5a098.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2408,"likes":392,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36120,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143332,"name":"天眼平台自动化测试实操演示","sourceCourseId":49143323,"description":null,"code":"20181228_000114","duration":24,"period":0.53,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/12/28/9d426091-71fe-45c1-a10d-fcfffcf06621.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1695,"likes":142,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36119,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143331,"name":"天眼平台统一监控实操演示","sourceCourseId":49143324,"description":null,"code":"20181228_000113","duration":26,"period":0.58,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/12/28/978e7def-a786-4358-aad5-94693a15805e.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1662,"likes":143,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36118,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143330,"name":"天眼平台补天运行支撑平台实操演示","sourceCourseId":49143325,"description":null,"code":"20181228_000112","duration":19,"period":0.42,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/12/28/e7ad2014-b362-4f7b-8b0f-284b6afc89f2.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1651,"likes":138,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36117,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143329,"name":"天眼平台","sourceCourseId":49143326,"description":null,"code":"20181228_000111","duration":16,"period":0.36,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/12/28/7648d892-ea11-42ed-834b-ac14e934c1cd.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2505,"likes":406,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36116,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49143328,"name":"B域能力开放平台研发调用与联调","sourceCourseId":49143327,"description":null,"code":"20181228_000110","duration":43,"period":0.96,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/12/28/68175b7d-7fca-4848-bb41-11f8fa2c6d7e.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1651,"likes":146,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":36115,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142781,"name":"敏捷研发全流程实战","sourceCourseId":49142753,"description":null,"code":"20181114_001169","duration":67,"period":1.49,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/9ad033e0-7a98-440c-b17a-95f1519a37c5.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2006,"likes":191,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35568,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":true,"courseGroupId":null,"groupName":null},{"id":49142788,"name":"天梯总体介绍及工具串讲（上）","sourceCourseId":49142746,"description":null,"code":"20181114_001176","duration":44,"period":0.98,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/19c044eb-7d42-451f-ac75-85bd7de61b33.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":3285,"likes":469,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35575,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142789,"name":"天梯总体介绍及工具串讲（下）","sourceCourseId":49142745,"description":null,"code":"20181114_001177","duration":44,"period":0.98,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/223bf789-c493-4c94-ad61-8ec66d47cc05.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":3055,"likes":453,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35576,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142786,"name":"天宫平台概述","sourceCourseId":49142748,"description":null,"code":"20181114_001174","duration":59,"period":1.31,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/908d4ed6-c9a1-4b0e-82a7-d87e7aaa2fb4.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":3572,"likes":488,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35573,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142782,"name":"天宫DCOS基础","sourceCourseId":49142752,"description":null,"code":"20181114_001170","duration":116,"period":2.58,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/c0e92f3b-0e79-4826-a37a-ab0ebc89f584.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1892,"likes":167,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35569,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142783,"name":"天宫DCOS监控培训","sourceCourseId":49142751,"description":null,"code":"20181114_001171","duration":71,"period":1.58,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/0c8bcf91-385b-4c84-bfe7-1eb4fa63a4ee.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1819,"likes":168,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35570,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142780,"name":"Docker基础及实操","sourceCourseId":49142754,"description":null,"code":"20181114_001168","duration":55,"period":1.22,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/0d05d3c1-1502-4af3-8ca5-37e5b5c8feab.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2854,"likes":447,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35567,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142785,"name":"天宫平台服务培训","sourceCourseId":49142749,"description":null,"code":"20181114_001173","duration":62,"period":1.38,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/c95156b0-680e-4325-9393-a0e830b48555.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2894,"likes":421,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35572,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142787,"name":"天宫平台组件培训","sourceCourseId":49142747,"description":null,"code":"20181114_001175","duration":36,"period":0.8,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/511969d6-db46-45de-8811-2fd6490d482e.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2593,"likes":409,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35574,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142784,"name":"天宫门户及入驻流程","sourceCourseId":49142750,"description":null,"code":"20181114_001172","duration":50,"period":1.11,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/340cfab7-2914-4429-887f-4d330aaaf788.png","categoryId":23196360,"categoryName":"其他","point":null,"learners":1761,"likes":163,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35571,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142771,"name":"天舟微服务(SkyArk)-方案介绍","sourceCourseId":49142764,"description":null,"code":"20181114_001159","duration":46,"period":1.02,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/e4db2d92-abcb-4906-9299-561adff8dbb0.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2575,"likes":413,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35558,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142772,"name":"开启微服务之旅-Springboot开发入门","sourceCourseId":49142763,"description":null,"code":"20181114_001160","duration":52,"period":1.16,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/d1e107a9-dd5c-47e3-a674-5fc849686869.png","categoryId":23196360,"categoryName":"其他","point":null,"learners":1703,"likes":150,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35559,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142774,"name":"Springboot工程部署到天舟平台","sourceCourseId":49142760,"description":null,"code":"20181114_001162","duration":47,"period":1.04,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/337e5769-e673-4bd6-8c8e-2651b0dd9a57.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1702,"likes":153,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35561,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142777,"name":"天舟平台微服务开发基础","sourceCourseId":49142757,"description":null,"code":"20181114_001165","duration":51,"period":1.13,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/de7e0c04-782a-448e-ba1b-db7a5c9ac0f0.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2550,"likes":416,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35564,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142779,"name":"天舟平台微服务开发进阶","sourceCourseId":49142755,"description":null,"code":"20181114_001167","duration":60,"period":1.33,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/66e729f0-b71c-44e9-af53-706886cf6ab8.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":2853,"likes":469,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35566,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142770,"name":"天梯平台上机实战-管理组","sourceCourseId":49142765,"description":null,"code":"20181114_001158","duration":47,"period":1.04,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/cc780723-2959-46f9-9fc3-7ab936e1b231.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1688,"likes":144,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35557,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142773,"name":"天梯平台上机实战-需求组","sourceCourseId":49142761,"description":null,"code":"20181114_001161","duration":20,"period":0.44,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/f8d55083-ee62-4510-8b37-958d054ed69f.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1662,"likes":149,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35560,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142775,"name":"天梯平台上机实战-研发组","sourceCourseId":49142759,"description":null,"code":"20181114_001163","duration":22,"period":0.49,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/6a35b0ae-f9d5-4d6f-99f8-6b0ca0ab06c0.jpg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1664,"likes":146,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35562,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142776,"name":"天梯平台上机实战-测试组","sourceCourseId":49142758,"description":null,"code":"20181114_001164","duration":31,"period":0.69,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/dc5cb627-0d75-4fe6-a547-730493215834.jpeg","categoryId":23196360,"categoryName":"其他","point":null,"learners":1658,"likes":147,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35563,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null},{"id":49142778,"name":"天梯平台上机实战-版本组","sourceCourseId":49142756,"description":null,"code":"20181114_001166","duration":26,"period":0.58,"progress":100.0,"version":null,"status":"C","imageUrl":"/content/upload/2018/11/13/4d80c5da-a567-42ec-ade7-c9d21557b8cb.png","categoryId":23196360,"categoryName":"其他","point":null,"learners":1668,"likes":155,"courseType":"ONLINE","platform":"ALL","platforms":null,"rcoId":null,"offeringCourseId":35565,"courseCollectionId":null,"isArchived":false,"isCollected":false,"isLiked":false,"courseGroupId":null,"groupName":null}]}</pre></body></html>
        """
        return html

    @staticmethod
    def html_to_json(html):
        # html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        json_text = soup.body.text
        return json.loads(json_text)


# 两种不同url
# https://www.jianshu.com/p/9cd222f65efa?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
# https://www.jianshu.com/p/f9fb7ea4bf32



if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    for i, val in enumerate(list1):
        print("序号：", i, "  值：", val)

    # html = Test.get_html()
    # dict1 = Test.html_to_json(html)
    # print(dict1)

    # list1 = Test.start_req()
    # for lis in list1:
    #     print(lis)
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

    # html = """
    # <span style="color: rgb(0, 51, 51); size: 2px; text-decoration: none; cursor: pointer;"
    # onmouseover="this.style.color=&quot;#ff3333&quot;"
    # onmouseout="this.style.color=&quot;#003333&quot;"
    # onclick="window.open(&quot;/jsp/cnceb/web/info1/detailNotice.jsp?id=2875703300000014418&quot;,&quot;&quot;,&quot;
    # height=600,width=900,left=60,toolbar=yes,
    # menubar=yes,scrollbars=yes,resizable=yes,status=yes&quot;);"
    # title="2019年中国联通广东湛江LTEFDD室分口碑场景新建一期工程湛江工程项目直放站采购项目(第二次）竞争性谈判公告">2019年中国联通广东湛江LTEFDD室分口碑场景新建一期工程湛江工程...
	#
	# 								</span>
    # """
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


