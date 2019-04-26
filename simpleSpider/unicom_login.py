# coding = utf-8

import requests
from lxml import etree
import pytesseract
from PIL import Image
from urllib import request
import os
# ## 失败 ###
# ## 成功 请见： D:\python\python_spider\selenium\unicom_oa_login.py ###


class UserAutoLogin(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/71.0.3578.98 Safari/537.36',
                        'Referer': 'http://sso.portal.unicom.local/eip_sso/ssoLogin.html?appid=np000&success=http://www.portal.unicom.local/user/token'
                        }
        # self.get_url = 'http://sso.portal.unicom.local/eip_sso/ssoLogin.html?appid=np000&success=http%3A%2F%2Fwww.portal.unicom.local%2Fuser%2Ftoken&error=http%3A%2F%2Fwww.portal.unicom.local%2Fuser%2Ferror&return=http%3A%2F%2Fwww.portal.unicom.local%2F'
        self.get_url = 'http://sso.portal.unicom.local/eip_sso/ssoLogin.html?appid=np000&success=http://www.portal.unicom.local/user/token'

        self.post_url = 'http://sso.portal.unicom.local/eip_sso/rest/authentication/login'

        self.ajax_url = 'http://www.portal.unicom.local/user/token?ajax=true'

        # 目录
        self.path = os.path.dirname(__file__)

    def login_auto(self):
        # print(self.path)

        response = requests.get(self.get_url, headers=self.headers)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        img = html.xpath('//img[@id="verifyCodeImg"]/@src')[0]
        img_url = 'http://sso.portal.unicom.local/eip_sso/'+img
        image_name = 'verifyCode.jpg'
        # 保存图片
        request.urlretrieve(img_url, os.path.join(self.path, image_name))

        # 识别图片
        image_object = Image.open('verifyCode.jpg')
        verify_code = pytesseract.image_to_string(image_object)
        verify_code = verify_code.replace(' ', '')
        print(verify_code)

        # print(img_file_name)

        # user_name = input('请输入用户名:')
        # user_pwd = input('请输入密码:')
        # verify_code = input('请输入验证码:')
        #
        # data = {'login': user_name, 'password': user_pwd, 'verifyCode': verify_code}
        # response = requests.post(self.post_url, data=data, headers=self.headers)
        # print(response.text)

        data = {'login': 'xuwy30',
                'password': 'xiaoxiG00DQAZ',
                'verify_code': verify_code,
                'appid': 'np000',
                'success': 'http://www.portal.unicom.local/user/token',
                'error': 'http://sso.portal.unicom.local:80/eip_sso/ssoLogin.html',
                'formFlag': '1',
                'accountid': 'xuwy30',
                'errorMsg': '',
                'errorCode': '25',
                'return': 'http://www.portal.unicom.local/'
                }
        print(data)
        response = requests.post(self.post_url, data=data, headers=self.headers)
        response.encoding = 'utf-8'
        print(response.text)

    # def login_test2(self):
    #     data = dict()
    #     api_str = '<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">' \
    #               '<soap:Body>' \
    #               '<saml:AssertionIDRequest xmlns=\"urn:oasis:names:tc:SAML:2.0:protocol\" xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\" xmlns:saml=\"urn:oasis:names:tc:SAML:2.0:assertion\" ID=\"1556194763661u0FIIrbOxuuCsHzvhPt7HeJgd\" Version=\"2.0\" IssueInstant=\"2019-04-25T20:19:23.661+08:00\">' \
    #               '<saml:AssertionIDRef>1556194763661NuuPbvKvMvhviHEaAny6czi4J</saml:AssertionIDRef>' \
    #               '</saml:AssertionIDRequest>' \
    #               '</soap:Body>' \
    #               '</soap:Envelope>'
    #     data = {'token', api_str}
    #     print(data)
    #     response = requests.post(self.ajax_url, data=data, headers=self.headers)
    #     # response.encoding = 'utf-8'
    #     print(response.text)



if __name__ == '__main__':
    userLogin = UserAutoLogin()
    userLogin.login_auto()





    # userLogin = UserAutoLogin()
    # userLogin.login_auto()


