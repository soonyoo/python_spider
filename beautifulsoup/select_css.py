# coding = utf-8
from bs4 import BeautifulSoup


class CssSelect(object):
    def __init__(self):
        self.html = """
        <table class="tablelist" cellpadding="0" cellspacing="0">
            <tbody>
                <tr class="h">
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
        </table> """

    def get_data_1(self):
        """
        # 1.获取所有tr标签
        :return:
        """
        soup = BeautifulSoup(self.html, 'lxml')
        trs = soup.select('tr')
        for tr in trs:
            print(tr)
            print('='*40)

    def get_data_2(self):
        """
        2.获取第2个tr标签
        :return:
        """
        soup = BeautifulSoup(self.html, 'lxml')
        tr = soup.select('tr')[1]
        print(tr)

    def get_data_3(self):
        """
        3.获取所有class等于even的tr标签
        :return:
        """
        soup = BeautifulSoup(self.html, 'lxml')
        # trs = soup.select('tr.even')
        # trs = soup.select('.even')  # 因为class="even" 的只有tr标签
        trs = soup.select("tr[class='even']")
        for tr in trs:
            print(tr)
            print('==' * 30)

    def get_data_4(self):
        """
        5. 获取所有a标签的href属性
        :return:
        """
        soup = BeautifulSoup(self.html, 'lxml')
        a_list = soup.select('a')
        for a in a_list:
            print(a['href'])
            # print(a.attrs['href'])

    def get_data_5(self):
        """
        6，获取所有的职位信息并且是纯文本
        :return:
        """
        soup = BeautifulSoup(self.html, 'lxml')
        trs = soup.select('tr')[1:]  # 跳过第一行(标题行)
        for tr in trs:
            infos = list(tr.stripped_strings)
            print(infos)




if __name__ == '__main__':
    css_select = CssSelect()
    # css_select.get_data_1()
    # css_select.get_data_2()
    # css_select.get_data_3()
    # css_select.get_data_4()
    css_select.get_data_5()


