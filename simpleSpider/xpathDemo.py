# coding = utf-8

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一段落</a></li>
         <li class="item-1"><a href="link2.html">第二段落</a></li>
         <li class="item-inactive"><a href="link3.html">第三段落</a></li>
         <li class="item-1"><a href="link4.html">第四段落</a></li>
         <li class="item-0"><a href="link5.html">第五段落</a>
     </ul>
</div>
'''


class XpathAndLxml:
    def __init__(self):
        self.result = ''

    # 解析 HTML 代码段
    '''
    首先我们使用 lxml 的 etree 库，然后利用 etree.HTML 初始化，然后我们将其打印出来。
    其中，这里体现了 lxml 的一个非常实用的功能就是自动修正 html 代码，
    大家应该注意到了，最后一个 li 标签，其实我把尾标签删掉了，是不闭合的。
    不过，lxml 因为继承了 libxml2 的特性，具有自动修正 HTML 代码的功能。
    '''
    def parse_text(self):
        html = etree.HTML(text)
        # encode/decode 为了防止中文乱码
        self.result = etree.tostring(html, encoding='utf-8').decode('utf-8')
        return self.result

    # 解析html文件
    def parse_html(self, file_name):
        html = etree.parse(file_name)
        self.result = etree.tostring(html, encoding='utf-8').decode('utf-8')
        return self.result

    # 增加解析器参数，防止html不规范导致的报错。
    def good_parse_html(self, file_name):
        parser = etree.HTMLParser(encoding='utf-8')
        html = etree.parse(file_name, parser=parser)  # 指定是HTML解析器
        # self.result = etree.tostring(html, encoding='utf-8').decode('utf-8')
        # return self.result
        return html


if __name__ == '__main__':
    x = XpathAndLxml()
    # print(x.parse_text())
    # print(x.parse_html('xpath.html'))
    # print(x.good_parse_html('xpath.html'))
    html = x.good_parse_html('tencent.html')

    # 1.获取所有tr标签
    # trs = html.xpath('//tr')
    # print(trs)
    # for tr in trs:
    #     tr_str = etree.tostring(tr, encoding='utf-8').decode('utf-8')
    #     print(tr_str)

    # 2.获取第2个tr标签
    #   注意：
    #   2.1 xx.xpath返回的数据类型为list(<class 'list'>)
    #   2.2 xx.xpath索引从1开始
    # trs = html.xpath('//tr')[2]
    # tr_str = etree.tostring(trs, encoding='utf-8').decode('utf-8')
    # print(tr_str)

    # 3.获取tr中class等于even的标签
    # trs = html.xpath("//tr[@class='even']")
    # for tr in trs:
    #     tr_str = etree.tostring(tr, encoding='utf-8').decode('utf-8')
    #     print(tr_str)

    # 4.获取所有a标签的href属性
    # a_tags = html.xpath('//tr//a/@href')
    # for a_tag in a_tags:
    #     print(a_tag)

    # 5.获取所有职位信息(纯文本)
    # a_texts = html.xpath('//tr//a/text()')
    a_texts = html.xpath('//tr/td[1]//text()')
    print(type(a_texts))
    # for text in a_texts:
    #     print(text)




