# coding = utf-8
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import requests
# from lxml import etree
# from urllib import request
from PIL import Image
import os
import pytesseract
import time
from selenium.webdriver.support import expected_conditions as EC   # 用于右键点击图片
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pyautogui


class OALogin(object):
    def __init__(self):
        self.home_url = 'http://sso.portal.unicom.local/eip_sso/ssoLogin.html?appid=np000&success=http://www.portal.unicom.local/user/token'
        self.driver_path = r'D:\python\chromedriver\chromedriver.exe'
        self.img_path = r'C:\Users\64174\Downloads\ValidateImage.jpg'
        # 判断文件是否存在(如果存在，删除)
        if os.path.exists(self.img_path):
            os.remove(self.img_path)
            print('成功移除文件：%s' % self.img_path)

    def login_auto(self):
        # 第1步：打开浏览器
        browser = webdriver.Chrome(executable_path=self.driver_path)
        browser.get(self.home_url)
        wait = WebDriverWait(browser, 10)

        # 第2步：输入用户名、密码、验证码
        # ## 2.1 查找[用户名]的输入框,并输入[用户名]
        browser.find_element_by_id('login').send_keys('xuwy30')
        time.sleep(1)
        # ## 2.2 查找[密码]的输入框,并输入[密码]
        browser.find_element_by_id('password').send_keys('xiaoxiG00DQAZ')
        time.sleep(1)

        # 第3步：保存图片，识别图片，输入识别码
        # 3.1 右键单击图片
        img = wait.until(EC.element_to_be_clickable((By.ID, 'verifyCodeImg')))
        # 3.2 执行鼠标动作
        actions = ActionChains(browser)
        # 3.3 找到图片后右键单击图片
        actions.context_click(img)
        time.sleep(1)
        actions.perform()
        # 3.4 找到图片另存为菜单
        time.sleep(1)
        # 3.5 向下走两个到了【图片另存为】
        pyautogui.typewrite(['down', 'down', 'enter'])
        # 3.6 单击图片另存之后等2s敲回车，存到chorme的默认下载路径：C:\Users\64174\Downloads\
        time.sleep(2)
        pyautogui.typewrite(['enter'])
        time.sleep(2)

        # 3.7 如果图片存在才进行识别
        if os.path.exists(self.img_path):
            # ##识别图片##
            image_object = Image.open(self.img_path)
            verify_code = pytesseract.image_to_string(image_object)
            # 防止有空格
            verify_code = verify_code.replace(' ', '')
            print(verify_code)
            # 3.7.1 判断长度为4位才进行验证码输入
            if len(verify_code) == 4:
                # ## 3.7.2 查找[验证码]的输入框,并输入[验证码]
                browser.find_element_by_id('verifyCode').send_keys(verify_code)
                time.sleep(1)
                # 第4步：点击登陆OK
                browser.find_element_by_xpath("//*[@id='loginForm']/div/div/a").click()
            time.sleep(30)


if __name__ == '__main__':
    userLogin = OALogin()
    userLogin.login_auto()
