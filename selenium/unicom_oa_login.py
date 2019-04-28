# coding = utf-8
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import requests
from lxml import etree
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
import json
from bs4 import BeautifulSoup
from urllib import request


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
        time.sleep(4)

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
                time.sleep(10)
                # 第4步搜索[学院]
                search_input = browser.find_element(By.ID, 'seachKey')
                search_input.send_keys('学院')
                # 点击搜索应用
                browser.find_element_by_xpath('//*[@id="page-top"]/div[2]/dl/dd/p[1]/a[1]').click()
                time.sleep(3)
                # 点击网络学院
                browser.find_element_by_xpath('//*[@id="page-body"]/div[2]/div/div/div/a').click()
                # print(browser.window_handles)
                browser.switch_to.window(browser.window_handles[1])
                # print(browser.current_url)
                time.sleep(10)
                # 点击,进入[网络学院]
                browser.find_element_by_xpath('/html/body/spk-root/spk-select-system/div/div/div/a[1]').click()
                time.sleep(10)
                # 访问播放地址
                # ##构造播放地址

                browser.get('http://wsxy.chinaunicom.cn/api/learner/subject/49651475/courses?status=&groupId=&page=0&size=50&name=')
                html = browser.page_source
                soup = BeautifulSoup(html, 'lxml')
                json_text = soup.body.text
                json_text_dict = json.loads(json_text)
                # print(type(json_text_dict))

                course_content_lists = json_text_dict["content"]

                # 构造播放地址
                # http://wsxy.chinaunicom.cn/learner/play/course/49143893;classroomId=49651475;courseDetailId=36680;
                ### 49143893 = json中的ID
                ### classroomId = 专题ID
                ### courseDetailId = json中的offeringCourseId

                mp4_path_list = []
                mp4_dict = dict()

                for lis in course_content_lists:
                    class_id = lis['id']
                    classroom_id = '49651475'
                    course_detail_id = lis['offeringCourseId']
                    class_name = lis['name']
                    class_url = 'http://wsxy.chinaunicom.cn/learner/play/course/%s;classroomId=%s;courseDetailId=%s;' % (class_id, classroom_id, course_detail_id)
                    browser.get(class_url)
                    time.sleep(10)
                    html = etree.HTML(browser.page_source)
                    mp4_url = html.xpath('//iframe/@src')[0]
                    # 获取mp4完整地址 print(mp4_url)
                    begin_url = mp4_url.index('=/content')
                    end_url = mp4_url.index('.mp4')
                    url = mp4_url[begin_url + 1:end_url + 4]
                    mp4_full_path = 'http://content.wsxy.chinaunicom.com' + url
                    # 把mp4地址存起来
                    mp4_dict["cn_name"] = class_name
                    mp4_dict["mp4_url"] = mp4_full_path
                    mp4_path_list.append(mp4_dict)
                    print(mp4_dict)
                    mp4_dict = {}
                    # 等2秒退出
                    time.sleep(2)
                    browser.find_element_by_css_selector('.back-course').click()
                    time.sleep(6)

                # print(mp4_path_list)
                return mp4_path_list
                # time.sleep(30)
            else:
                return None
                print('图片识别失败...')
        else:
            return None
            print("图片不存在...")

    # 防止网络不好，重新下载
    def auto_down(self, url, filename):
        try:
            request.urlretrieve(url, filename)
        except request.ContentTooShortError:
            print('Network conditions is not good.Reloading.')
            self.auto_down(url, filename)

    # 下载
    def down_load_mp4(self):
        list_mp4 = self.login_auto()
        # print(os.path.dirname(__file__))
        # with open('class_json_file.json', 'r', encoding='utf-8') as fp:
        #     list_mp4 = json.load(fp)
        # print(type(list_mp4))
        if len(list_mp4) > 0:
            for lis in list_mp4:
                cn_name = lis["cn_name"]
                file_name = r"D:\tiangong_movie\%s.mp4" % cn_name
                begin_msg = 'download [%s] bigin ....' % cn_name
                end_msg = '[%s] download complete ' % cn_name
                print(begin_msg)
                request.urlretrieve(lis["mp4_url"], file_name)
                print(end_msg)


if __name__ == '__main__':
    userLogin = OALogin()
    userLogin.down_load_mp4()
