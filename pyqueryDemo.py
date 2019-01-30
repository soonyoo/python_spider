# coding=utf-8

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


# 提取html代码段的li标签
def get_html_li():
    doc = pq(html)
    print(doc('li'))


# 从URL中解析html源码
def get_html_from_url():
    doc = pq(url='http://www.baidu.com', encoding="utf-8")  # 增加encoding="utf-8"，防止中文乱码
    print(doc('head'))


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
    get_html_text()
