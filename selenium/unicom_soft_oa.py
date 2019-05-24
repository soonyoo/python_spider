# coding = utf-8

from selenium import webdriver
import time


class GzSoftLogin(object):
    def __init__(self):
        self.url = 'http://10.245.47.1/portal/#/login'
        self.driver_path = r'D:\python\chromedriver\chromedriver.exe'

    def login_auto(self):
        # 第1步：打开浏览器
        browser = webdriver.Chrome(executable_path=self.driver_path)
        browser.get(self.url)
        time.sleep(1)
        browser.find_element_by_id('argusername').send_keys('###')
        browser.find_element_by_id('arguserpass').send_keys('###')
        time.sleep(2)
        idcode = input('请手工输入验证码：')
        browser.find_element_by_id('idcode').send_keys(idcode)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[3]/div/div/form/button').click()

        time.sleep(30)


        # html = browser.page_source
        # print(html)


if __name__ == '__main__':
    gz_soft = GzSoftLogin()
    gz_soft.login_auto()



