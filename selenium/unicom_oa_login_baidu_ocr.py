# coding = utf-8
from selenium import webdriver
import os
import time
from selenium.webdriver.support import expected_conditions as EC   # 用于右键点击图片
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pyautogui
import yaml
from common.baidu_api_util import BaiduOCR

"""使用baiduOCR识别OA中的图片验证，并登陆到网上学院网站。
@author: xuwenyuan
@date: 2019-09-06
"""

class OALogin(object):
    def __init__(self):
        self.home_url = 'http://sso.portal.unicom.local/eip_sso/ssoLogin.html?appid=np000&success=http://www.portal.unicom.local/user/token'
        self.driver_path = r'D:\python\chromedriver\76.0.3809.12\chromedriver.exe'
        self.img_path = 'C:/Users/64174/Downloads/ValidateImage.jfif'
        self.base_mp4_url = 'http://content.wsxy.chinaunicom.com'
        self.class_api_url = 'http://wsxy.chinaunicom.cn/api/learner/subject/49651475/courses?status=&groupId=&page=0&size=50&name='
        self.base_class_url = 'http://wsxy.chinaunicom.cn/learner/play/course'
        # 判断文件是否存在(如果存在，删除)
        if os.path.exists(self.img_path):
            os.remove(self.img_path)
            print('成功移除文件：%s' % self.img_path)

    #
    @staticmethod
    def read_yaml_file():
        """
        读取配置文件:unicom_oa_config.yaml
        配置文件中存有用户名和密码
        :return:
        """
        cur_path = os.path.dirname(os.path.realpath(__file__))
        yaml_file = os.path.join(cur_path, "unicom_oa_config.yaml")
        with open(yaml_file, 'r', encoding='utf-8') as fp:
            cfg = fp.read()
            cfg_dict = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
        return cfg_dict

    def login_auto(self):
        # 第1步：打开浏览器
        browser = webdriver.Chrome(executable_path=self.driver_path)
        browser.get(self.home_url)
        wait = WebDriverWait(browser, 10)

        # 第2步：输入用户名、密码、验证码
        # ## 2.1 查找[用户名]的输入框,并输入[用户名]
        user_info = OALogin.read_yaml_file()
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
            baidu_ocr = BaiduOCR()
            verify_code = baidu_ocr.get_img_text(self.img_path)
            print(verify_code)
            if verify_code is None:
                print('图片识别失败！None...')
                browser.close()
            elif len(verify_code) != 4:
                print('图片识别失败！长度不正确...')
                browser.close()
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
                time.sleep(100)
                browser.close()

if __name__ == '__main__':
    userLogin = OALogin()
    userLogin.login_auto()
