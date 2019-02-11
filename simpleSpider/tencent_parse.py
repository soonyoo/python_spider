# coding = utf-8
from lxml import etree

"""
使用xpath技术抓取tencent.html文件中的内容，并分析出所需要的字段内容。
"""


class GetTencentInfo:
    def __init__(self):
        self.advertise_list = []
        self.position_info = {}

    # 解析html文件
    @staticmethod
    def parse_html(file_name):
        parser = etree.HTMLParser(encoding='utf-8')
        html = etree.parse(file_name, parser=parser)
        # self.result = etree.tostring(html, encoding='utf-8').decode('utf-8')
        # 返回类型<class 'lxml.etree._ElementTree'> 才能使用.xpath
        return html

    # 获取所需要的数据
    def parse_tencent_data(self):
        html = GetTencentInfo.parse_html('tencent.html')
        tr_lists = html.xpath('//tr[position()>1]')
        # xpath 返回的数据类型为：<class 'list'>
        for tr_single in tr_lists:
            self.position_info["position_name"] = tr_single.xpath('./td[1]//text()')[0]
            self.position_info["position_type"] = tr_single.xpath('./td[2]//text()')[0]
            self.position_info["nums"] = tr_single.xpath('./td[3]//text()')[0]
            self.position_info["address"] = tr_single.xpath('./td[4]//text()')[0]
            self.position_info["pubdate"] = tr_single.xpath('./td[5]//text()')[0]
            self.advertise_list.append(self.position_info)
            self.position_info = {}
        return self.advertise_list


if __name__ == '__main__':
    tencent = GetTencentInfo()
    lists = tencent.parse_tencent_data()
    for i in range(len(lists)):
        # print(lists[i])
        print('职位名称: %(position_name)s\t职位类别：%(position_type)s\t人数: %(nums)s\t地点：%(address)s\t发布时间：%(pubdate)s' % (lists[i]))