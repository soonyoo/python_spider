# coding = utf-8
import re

# 教程位置
# D:\python\video\2019Python\python网络爬虫全套\
# 03.第三阶段 Python分布式爬虫框架应用\
# 05.Python爬虫之XPath多线程视频教程 13课
# \1.基本的正则表达式


# 读取文件
def read_file(file_name):
    f = open(file_name, 'r', encoding='UTF-8')
    html = f.read()
    f.close()
    return html


# 读取标题
def find_title():
    html = read_file("1.txt")
    title = re.search("<title>(.*?)</title>", html, re.S).group(1)
    # return title
    print(title)


# 爬取a标签内容
def find_a():
    html = read_file("1.txt")
    links = re.findall('href="(.*?)"', html, re.S)
    for link in links:
        print(link)


# 爬取a标签href内容 并过滤了welcome部分
def find_a_ul():
    html = read_file("1.txt")
    ul_html = re.findall('<ul>(.*?)</ul>', html, re.S)[0]
    links = re.findall('href="(.*?)"', ul_html, re.S)
    for link in links:
        print(link)


# 爬取<a>**</a>中间部分内容
def find_a_text_ul():
    html = read_file("1.txt")
    ul_html = re.findall('<ul>(.*?)</ul>', html, re.S)[0]
    links = re.findall('">(.*?)</a>', ul_html, re.S)
    for link in links:
        print(link)




if __name__ == "__main__":
    # find_a_ul()
    # find_title()
    find_a_text_ul()






