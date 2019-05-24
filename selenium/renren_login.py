# coding = utf-8
from selenium import webdriver

import time


class RenrenLogin(object):
    def __init__(self):
        self.home_url = 'http://www.renren.com/'
        self.driver_path = r'D:\python\chromedriver\chromedriver.exe'

    def login_renren(self):
        # 第1步：打开浏览器
        browser = webdriver.Chrome(executable_path=self.driver_path)
        browser.get(self.home_url)
        browser.find_element_by_id('email').send_keys('你的人人网帐号')
        time.sleep(2)
        browser.find_element_by_id('password').send_keys('你的密码')
        time.sleep(2)
        browser.find_element_by_id('login').click()
        # sleep50秒，演示、测试用
        time.sleep(50)


if __name__ == '__main__':
    login = RenrenLogin()
    login.login_renren()
