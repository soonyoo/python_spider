# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from lxml import etree
import csv



class WO(object):
    def __init__(self):
        self.login_url ='https://zqhd.chainew.com/flowq/front/account/passwordLogin'
        self.driver_path = r'D:\python\chromedriver\chromedriver.exe'

    @staticmethod
    def save_html(file_name, file_content):
        with open(file_name.replace('/', '_') + '.html', 'wb') as f:
            f.write(file_content)

    @staticmethod
    def write_to_csv(headers_list, values_dict_list, file_name):
        """
        保存到csv文件函数
        :param headers_list:
        :param values_dict_list:
        :param file_name:
        :return:
        """
        with open(file_name, 'w', encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, headers_list)
            # 写入表头数据时，需要调用writeheader方法
            writer.writeheader()
            writer.writerows(values_dict_list)

    def login_wo(self):
        # 第1步：打开浏览器
        browser = webdriver.Chrome(executable_path=self.driver_path)
        browser.get(self.login_url)
        wait = WebDriverWait(browser, 10)

        # 第2步：输入用户名、密码、验证码
        # ## 2.1 查找[用户名]的输入框,并输入[用户名]
        browser.find_element_by_id('phoneNumber').send_keys('fs13250116688')
        time.sleep(1)
        # ## 2.2 查找[密码]的输入框,并输入[密码]
        browser.find_element_by_id('pwd').send_keys('Yuxm353866')
        time.sleep(1)

        # ##3.点击登陆
        browser.find_element_by_id('btnLoginPassword').click()
        time.sleep(2)

        # 4.点击个人中心
        browser.find_element_by_xpath("/html/body/div[3]/a[3]").click()
        time.sleep(3)


        # 5.点击我的订单

        # browser.find_element_by_xpath("/html/body/div[2]/a[3]").click()

        # 5.1 使用js脚本拖动到指定地方[我的订单]
        target = browser.find_element_by_xpath("/html/body/div[2]/a[3]")
        # 拖动到可见的元素去
        browser.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)
        # 5.2 点击[我的订单]
        target.click()
        time.sleep(3)
        # 6.点击 [14GB全国流量7天]
        browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]").click()
        time.sleep(2)

        # 保存数据
        content = browser.page_source
        html = etree.HTML(content)
        trs = html.xpath("//table[@id='queryData']/tbody/tr")[1:]
        # print(len(trs))

        wo_list = []
        wo_dict = dict()
        for tr in trs:
            tds = tr.xpath("./td")
            wo_dict['产品名称'] = tds[0].xpath('./text()')[0]
            wo_dict['手机号码'] = tds[1].xpath('./text()')[0]
            wo_dict['开通状态'] = tds[2].xpath('./text()')[0]
            wo_list.append(wo_dict)
            wo_dict = {}

        # print(wo_list)

        headers = ['产品名称', '手机号码', '开通状态']
        WO.write_to_csv(headers, wo_list, 'wo.csv')
        print('操作成功...')
        



        # print(html)
        # file_content = bytes(html, encoding="utf8")
        # WO.save_html('wo', file_content)

        # content = browser.page_source
        # print(content)
        """

        # 进入[我的订单]
        browser.get('https://zqhd.chainew.com/flowq/front/withdrawCashSQ/myOrderPage')
        time.sleep(4)

        browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]").click()
        time.sleep(8)

        # 保存数据
        # html = browser.page_source
        # file_content = bytes(html, encoding="utf8")
        # WO.save_html('wo', file_content)
        
        """
        # time.sleep(3000)


if __name__ == '__main__':
    wo = WO()
    wo.login_wo()

