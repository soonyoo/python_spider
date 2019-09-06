# coding = utf-8
import yaml
import os
from aip import AipOcr


"""OCR图片文字识别
@author: xuwenyuan
date: 2019-09-05
desc: 根据传入的图片(全路径)，识别出图片中的文字，主要用于验证码的识别
"""
class BaiduOCR(object):
    def __init__(self):
        file_path = os.path.dirname(__file__)
        yaml_file = os.path.join(file_path, 'baidu_api_conf.yml')
        with open(yaml_file, 'r', encoding='utf-8') as fp:
            content = fp.read()
            conf = yaml.load(content, Loader=yaml.FullLoader)
            # baiduOCRKey
            self.app_id = conf['baiduOCR']['app_id']
            self.api_key = conf['baiduOCR']['api_key']
            self.secret_key = conf['baiduOCR']['secret_key']
            self.client = AipOcr(self.app_id, self.api_key, self.secret_key)

    def get_img_text(self, img_name):
        """读取图片，并识别图片里面的文本
        :param img_name: 图片全路径
        :return: 返回文本
        {'log_id': 7202748421669539685, 'words_result_num': 1, 'words_result': [{'words': 'FWYP'}]}
        """
        with open(img_name, 'rb') as fp:
            result_dic = self.client.basicGeneral(fp.read())
            result = result_dic['words_result'][0]['words']
            result = result.replace(' ', '')
            return result


if __name__ == '__main__':
    baidu_ocr = BaiduOCR()
    img_text = baidu_ocr.get_img_text("C:/Users/64174/Downloads/ValidateImage.jfif")
    print(img_text)
