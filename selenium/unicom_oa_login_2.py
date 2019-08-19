# coding = utf-8
from selenium import webdriver
# from selenium.webdriver.common.keys import KeysWebDriverWait
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
import yaml
# import socket

class OALogin(object):
    def __init__(self):
        self.home_url = 'http://sso.portal.unicom.local/eip_sso/ssoLogin.html?appid=np000&success=http://www.portal.unicom.local/user/token'
        self.driver_path = r'D:\python\chromedriver\76.0.3809.12\chromedriver.exe'
        self.img_path = r'C:\Users\64174\Downloads\ValidateImage.jfif'
        # self.img_path = r'D:\python\python_spider\selenium\verifyCode.jpg'
        self.base_mp4_url = 'http://content.wsxy.chinaunicom.com'
        self.class_api_url = 'http://wsxy.chinaunicom.cn/api/learner/subject/49651475/courses?status=&groupId=&page=0&size=50&name='
        self.base_class_url = 'http://wsxy.chinaunicom.cn/learner/play/course'
        # 判断文件是否存在(如果存在，删除)
        if os.path.exists(self.img_path):
            os.remove(self.img_path)
            print('成功移除文件：%s' % self.img_path)

    # 验证码图片文字识别
    def ocr_identification_code(self):
        image_object = Image.open(self.img_path)
        verify_code = pytesseract.image_to_string(image_object)
        # 防止有空格
        verify_code = verify_code.replace(' ', '')
        # print(verify_code)
        return verify_code

    # 读取配置文件
    @staticmethod
    def read_yaml_file():
        # 获取yaml文件路径
        cur_path = os.path.dirname(os.path.realpath(__file__))
        yaml_file = os.path.join(cur_path, "unicom_oa_config.yaml")
        with open(yaml_file, 'r', encoding='utf-8') as fp:
            cfg = fp.read()
            cfg_dict = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
        return cfg_dict

    @staticmethod
    def html_to_json(html):
        # html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        json_text = soup.body.text
        return json.loads(json_text)

    @staticmethod
    def read_json_file(file_name, coding):
        """
        使用json.load读取json文件
        :param file_name: 文件名
        :param coding: 编码（如utf-8）
        :return: <class 'list'>
        """
        with open(file_name, 'r', encoding=coding) as fp:
            persons = json.load(fp)
        return persons

    @staticmethod
    def dump_save_file(json_string, file_name, coding):
        """
        使用dump函数，保存文件
        # json.dump(json_string, fp) 这样写会中文乱码，
        # 如果要保存含有中文的字符串，建议加上ensure_ascii=False,json.dump默认使用ascii字符码

        :param json_string: 要保存的json字符串
        :param file_name: 要保存的文件名称
        :param coding: 字符编码(如utf-8)
        :return: 没有返回值
        """
        with open(file_name, 'w', encoding=coding) as fp:
            json.dump(json_string, fp, ensure_ascii=False)

    # 返回播放地址url
    def get_class_url(self, class_id, classroom_id, course_detail_id):
        class_url = '/%s;classroomId=%s;courseDetailId=%s;' % (class_id, classroom_id, course_detail_id)
        class_url = self.base_class_url + class_url
        return class_url

    # 防止网络不好，重新下载
    @staticmethod
    def auto_down(list_mp4):

        OALogin.dump_save_file(list_mp4, 'd:/tiangong_movie/mp4.json', 'utf-8')

        for lis in list_mp4:
            # 文件夹是否存在，不存在，创建。
            dirs = 'd:/tiangong_movie/{}/'.format(lis['type'])
            if not os.path.exists(dirs):
                os.makedirs(dirs)

            cn_name = lis["cn_name"] + '.mp4'
            work_path = dirs + cn_name

            try:
                begin_msg = 'download [%s] bigin ....' % cn_name
                end_msg = '[%s] download complete ' % cn_name
                print(begin_msg)
                request.urlretrieve(lis['mp4_url'], work_path)
                print(end_msg)
            # 如果出现异常，打印日志，并继续往下
            except request.ContentTooShortError:
                print('Network conditions is not good.Reloading.')
                print(lis['mp4_url'])
                continue
            except Exception as result:
                print('wrong:错误信息2:{}'.format(result))

    # 下载
    def down_load_mp4(self):
        list_mp4 = self.login_auto()

        if list_mp4 is None:
            print('mp4列表获取失败...')
        else:
            try:
                OALogin.auto_down(list_mp4)
            except Exception as result1:
                print('wrong:错误信息1:{}'.format(result1))

    def login_auto(self):
        # 第1步：打开浏览器
        browser = webdriver.Chrome(executable_path=self.driver_path)
        browser.get(self.home_url)
        wait = WebDriverWait(browser, 10)

        # 第2步：输入用户名、密码、验证码
        # ## 2.1 查找[用户名]的输入框,并输入[用户名]
        user_info = OALogin.read_yaml_file()
        # print(user_info)
        # pass

        browser.find_element_by_id('login').send_keys(user_info['username'])
        time.sleep(1)
        # ## 2.2 查找[密码]的输入框,并输入[密码]
        browser.find_element_by_id('password').send_keys(user_info['password'])
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
            verify_code = self.ocr_identification_code()
            print(verify_code)
            if verify_code is None:
                print('图片识别失败！None...')
            elif len(verify_code) != 4:
                print('图片识别失败！长度不正确...')
            # 3.7.1 判断长度为4位才进行验证码输入
            else:
                # ## 3.7.2 查找[验证码]的输入框,并输入[验证码]
                browser.find_element_by_id('verifyCode').send_keys(verify_code)
                time.sleep(1)
                # 第4步：点击登陆OK
                browser.find_element_by_xpath("//*[@id='loginForm']/div/div/a").click()
                # time.sleep(10)
                # 4.1 显式等待[搜索框]出现，10秒
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'seachKey')))
                # 4.2 输入[学院]
                browser.find_element(By.ID, 'seachKey').send_keys('学院')
                # 4.3 点击[搜索应用]
                time.sleep(2)
                browser.find_element_by_xpath('//*[@id="page-top"]/div[2]/dl/dd/p[1]/a[1]').click()
                # 4.4 显示等待[网络学院]
                time.sleep(2)
                WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, 'sub_count_link-na058')))
                # 4.5 点击[网络学院]
                time.sleep(2)
                browser.find_element_by_xpath('//*[@id="page-body"]/div[2]/div/div/div/a').click()
                # 4.6 切换窗口
                browser.switch_to.window(browser.window_handles[1])
                # print(browser.current_url)
                # time.sleep(10)
                # 4.7 显示等待30秒
                WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/spk-root/spk-select-system/div/div/div/a[1]')))
                # 4.8 点击,进入[网络学院]
                browser.find_element_by_xpath('/html/body/spk-root/spk-select-system/div/div/div/a[1]').click()
                # time.sleep(10)
                # 4.9 显示等待20秒
                WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'nz-overlay-0')))
                # 4.10 访问播放地址
                # 4.10.1 构造播放地址(从返回json数据中获取相应信息)
                # 4.10.2 定义数组，存放MP4真实地址
                mp4_path_list = []
                mp4_dict = dict()
                # 循环播放，获取mp4地址
                movie_lists = OALogin.read_json_file('unicom_oa_data.json', 'utf-8')
                for lis in movie_lists:
                    # 访问第一级地址
                    # "http://wsxy.chinaunicom.cn/api/learner/offering-courses/35535"
                    # 获取35535
                    # print(lis['url'])
                    class_room_id = lis['url'].split("/")[-1]
                    # print(class_room_id)
                    api_url = "http://wsxy.chinaunicom.cn/api/learner/offering-courses/" + class_room_id
                    browser.get(api_url)
                    html = browser.page_source
                    json_text_dict = OALogin.html_to_json(html)
                    source_course_id = json_text_dict['sourceCourseId']

                    api_url = "http://wsxy.chinaunicom.cn/api/learner/course/{}/outline/tree".format(source_course_id)
                    browser.get(api_url)
                    html = browser.page_source
                    json_text_dict = OALogin.html_to_json(html)
                    url = json_text_dict['children'][0]['startingUrl']
                    mp4_dict["mp4_url"] = self.base_mp4_url + url
                    # 把mp4地址存起来
                    mp4_dict["cn_name"] = lis['title']
                    mp4_dict["type"] = lis['type']
                    mp4_path_list.append(mp4_dict)
                    # print(mp4_dict)
                    mp4_dict = {}
                return mp4_path_list


if __name__ == '__main__':
    userLogin = OALogin()
    # userLogin.login_auto()
    userLogin.down_load_mp4()
    # 测试识别
    # ocr = userLogin.ocr_identification_code()
    # print(ocr)
