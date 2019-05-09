# coding = utf-8
from lxml import etree

class Tmall(object):
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
    def parse_tmall_data(self):
        html = Tmall.parse_html('tmall.html')

        divs = html.xpath("//div[@id='J_ItemList']/div[@class='product  ']/div")
        if not divs:
            print('List Page error')
        for div in divs:
            goods_price= div.xpath("./p[@class='productPrice']/em/@title")[0]
            print(goods_price)
            break


if __name__ == '__main__':
    tmall = Tmall()
    tmall.parse_tmall_data()
