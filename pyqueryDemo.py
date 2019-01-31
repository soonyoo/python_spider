# coding=utf-8

import re
from pyquery import PyQuery as pq


html = ''' <div class="wrap">
   <div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul></div></div>'''

tangshi_html = "<span><a href=\"https://so.gushiwen.org/shiwenv_45c396367f59.aspx\" target=\"_blank\">行宫</a>(元稹)</span>"

tangshi_list = []

global  current_poem
current_poem = {}


# 提取html代码段的li标签
def get_html_li():
    doc = pq(html)
    print(doc('li'))


# 从URL中解析html源码
def get_html_from_url(url):
    doc = pq(url=url, encoding="utf-8")  # 增加encoding="utf-8"，防止中文乱码
    # print(doc('head'))
    return doc


# 读取文件
def read_file(file_name):
    f = open(file_name, 'r', encoding='UTF-8')
    txt = f.read()
    f.close()
    return txt


# 从文件中解析html源码
def get_html_from_file():
    # doc = pq(filename='1.txt') 中文问题没解决
    txt = read_file('1.txt')
    doc = pq(txt)
    print(doc('li'))


# 基本CSS选择器
def get_html_from_css_base():
    doc = pq(html)
    print(doc('#container .list li'))


# 从子元素中获取数据
def get_html_from_son_element():
    doc = pq(html)
    items = doc('.list')
    # print(items)
    # lis = items.find('li')  # find不要求是子元素，有在里面就可以
    lis = items.children('.active') #XX.children 子元素
    print(lis)


# 父元素parent
def get_html_from_parent():
    doc = pq(html)
    items = doc('.list')
    container = items.parent('#container')
    print(container)


# 父元素parents
def get_html_from_parents():
    doc = pq(html)
    items = doc('.list')
    # parents = items.parents()
    # print(parents)  #  两个父节点都分别打出来
    parent = items.parents('.wrap')  # 只选择class为wrap的数据
    print(parent)


# 兄弟元素
def get_html_from_brother():
    doc = pq(html)
    items = doc('.list .item-0.active')
    li = items.siblings()
    print(li)


# 获取属性
def get_html_attribute():
    doc = pq(html)
    a = doc('.item-0.active a')
    print(a)
    print(a.attr('href'))
    print(a.attr.href)


# 获取文本
def get_html_text():
    doc = pq(html)
    a = doc('.item-0.active a')
    print(a)
    txt = a.text()  # a 标签内的文本，不包括html标签
    print(txt)
    htm = a.html()  # a 标签内的html
    print(htm)


def get_tangshi_html():
    pass
    # doc = pq(tangshi_html)
    # span = doc('span').text()
    # # a = doc('span a')
    # matchObj = re.match(r'(.*)\((.*)\)', str(span))
    # # print(matchObj.group(1))
    # # print(matchObj.group(2))
    # # print(span.text())
    # current_poem = {}
    # if matchObj:
    #     current_poem["title"] = matchObj.group(1)
    #     current_poem["author"] = matchObj.group(2)
    #     current_poem["url"] =  a.attr.href
    #     tangshi_list.append(current_poem)
    #     current_poem = {}
    # return tangshi_list


def get_tangshi_300():
    current_poem = {}
    doc = get_html_from_url('http://www.gushiwen.org/gushi/tangshi.aspx')
    spans = doc('span').items()  # .items()方法，返回一个迭代对象。class 'generator'
    for span in spans:
        # 解析出作者
        author = re.search('</a>(.*?)</span>', str(span)).group(1)
        current_poem["author"] = author.replace('(', '').replace(')', '')  # 替换()
        # 1解析a标签
        # 1.1 解析出标题
        a = span('span a')
        current_poem["title"] = a.text()
        # 1.2 解析出标题
        current_poem["url"] = a.attr.href

        # 加入数组
        tangshi_list.append(current_poem)
        # 清空对象，进入下次循环赋值
        current_poem = {}
    return tangshi_list


if __name__ == '__main__':
    # get_html_li()
    # get_html_from_url()
    # get_html_from_file()
    # get_html_from_css_base()
    # get_html_from_son_element()
    # get_html_from_parent()
    # get_html_from_parents()
    # get_html_from_brother()
    # get_html_attribute()
    # get_html_text()
    # get_tangshi_html()
    # get_tangshi_300()
    # print(tangshi_list)

    lists = get_tangshi_300()
    for i in range(len(lists)):
        # print('序号：', i, '值：', lists[i])
        print('标题: %(title)s\t作者：%(author)s\tURL: %(url)s' % (lists[i]))
