import urllib.request
import ssl
import base64
# https://market.aliyun.com/products/?keywords=%E5%9B%BE%E7%89%87%E9%AA%8C%E8%AF%81%E7%A0%81%20%E8%AF%86%E5%88%AB


class AliyunMarketOCR(object):
    def __init__(self):
        self.host = 'https://imgurlocr.market.alicloudapi.com'
        self.path = '/urlimages'

    @staticmethod
    def get_file_content(image_url):
        with open(image_url, 'rb') as fp:
            return fp.read()

    @staticmethod
    def image_object(image_url):
        """
        1. 如果是网络图片,直接返回
        2. 如果是本地图片，加base64，返回
        :param image_url: 传入的图片参数
        :return: 返回的数据格式
        """
        if 'http' in image_url:
            return image_url
        else:  #
            image_file = AliyunMarketOCR.get_file_content(image_url)
            base64_image = base64.b64encode(image_file).decode()
            image_data = 'data:image/jpeg;base64,{}'.format(base64_image)
            return image_data

    def aliyun_ocr(self, image_url):
        """
        识别图片，并返回结果
        """
        method = 'POST'
        appcode = '089392f80f954f33bcde1a8ff2e0b747'
        querys = ''
        url = self.host + self.path
        bodys = dict()
        bodys['image'] = AliyunMarketOCR.image_object(image_url)

        post_data = urllib.parse.urlencode(bodys).encode(encoding='UTF8')
        request = urllib.request.Request(url, post_data)
        # 根据API的要求，定义相对应的Content-Type
        request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        request.add_header('Authorization', 'APPCODE ' + appcode)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        response = urllib.request.urlopen(request, context=ctx)
        content = response.read()
        return content.decode('UTF-8')


if __name__ == '__main__':
    aliyun_ocr = AliyunMarketOCR()
    # 1.网络图片
    image = 'https://fegine-drug.oss-cn-shanghai.aliyuncs.com/image/urlimage.png'

    # 2.本地图片
    # image = './abc.jpg'

    result = aliyun_ocr.aliyun_ocr(image)
    print(result)


