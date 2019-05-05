# coding = utf-8

from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
        <tbody><tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
                        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47441&amp;keywords=python&amp;tid=0&amp;lid=0">TME-全民K歌数据产品经理</a></td>
            <td>产品/项目类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-02-03</td>
        </tr>
                        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47442&amp;keywords=python&amp;tid=0&amp;lid=0">TME-全民K歌高级数据产品经理</a></td>
            <td>产品/项目类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-02-03</td>
        </tr>
                        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47428&amp;keywords=python&amp;tid=0&amp;lid=0">30628-腾讯广告算法高级工程师（研发中心-深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-02-03</td>
        </tr>
                        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47423&amp;keywords=python&amp;tid=0&amp;lid=0">TEG02-网络运维工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-02-03</td>
        </tr>
                        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47411&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云资深运营开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-02-03</td>
        </tr>
                        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47396&amp;keywords=python&amp;tid=0&amp;lid=0">PCG11-后台开发工程师（北京）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>北京</td>
            <td>2019-02-03</td>
        </tr>
                        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47379&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云serverless运营开发工程师（深圳总部）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-02-03</td>
        </tr>
                        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47380&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云serverless运营开发工程师（成都）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>成都</td>
            <td>2019-02-03</td>
        </tr>
                        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=47374&amp;keywords=python&amp;tid=0&amp;lid=0">18436-NLP算法研究员（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-02-03</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a class="test" id="test" target="_blank" href="position_detail.php?id=47359&amp;keywords=python&amp;tid=0&amp;lid=0">PCG17-QQ钱包后台开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-02-03</td>
        </tr>
    </tbody>
</table>
"""

soup = BeautifulSoup(html, 'lxml')
# 1.获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print(type(tr))
#     print('*'*30)
# 2.获取第2个tr标签
# tr = soup.find_all('tr', limit=2)[1]
# print(tr)
# 3.获取所有class等于even的tr标签
# 3.1 方法1（注意class => class_）
# trs = soup.find_all('tr', class_='even')
# for tr in trs:
#     print(tr)
#     print('='*30)
# 3.2 方法2（atrribute）
# trs = soup.find_all('tr', attrs={'class': 'even'})
# for tr in trs:
#     print(tr)
#     print('='*30)

# 4.将所有ID等于test,class也等于test的a标签提取出来。
# 4.1 方法一，把相关参数都传进去：
# aList = soup.find_all('a', id="test", class_='test')
# 4.2 方法二，通过属性的方式：
# aList = soup.find_all('a', attrs={"id": "test", "class": "test"})
# for a in aList:
#     print(a)
# 5. 获取所有a标签的href属性
# aList = soup.find_all('a')
# for a in aList:
#     # 5.1 通过下标的方式获取
#     # href = a["href"]
#     # print(href)
#     # print('='*30)
#     # 5.2 通过attrs属性的方式
#     href = a.attrs['href']
#     print(href)

# 6，获取所有的职位信息并且是纯文本

trs = soup.find_all('tr')[1:]
position_list = []
position_dict = {}
for tr in trs:
    # 6.1 方法一：
    # tds = tr.find_all('td')
    # position_dict["p_name"] = tds[0].string
    # position_dict['p_type'] = tds[1].string
    # position_dict['num'] = tds[2].string
    # position_dict['area'] = tds[3].string
    # position_dict['post_time'] = tds[4].string
    # position_list.append(position_dict)
    # position_dict = {}
    # 方法二 (tr.strings:返回带换行符的数组)
    # infos = list(tr.strings)
    # print(infos)
    #['\n', 'PCG17-QQ钱包后台开发工程师（深圳）', '\n', '技术类', '\n', '1', '\n', '深圳', '\n', '2019-02-03', '\n']
    # 方法三(stripped_strings)
    infos = list(tr.stripped_strings)
    # print(infos)
    position_dict["p_name"] = infos[0]
    position_dict['p_type'] = infos[1]
    position_dict['num'] = infos[2]
    position_dict['area'] = infos[3]
    position_dict['post_time'] = infos[4]
    position_list.append(position_dict)
    position_dict = {}
# print(position_list)
for p in position_list:
    print(p)
#










