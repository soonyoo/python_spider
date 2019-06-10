import urllib.request
import ssl
import base64

# https://market.aliyun.com/products/?keywords=%E5%9B%BE%E7%89%87%E9%AA%8C%E8%AF%81%E7%A0%81%20%E8%AF%86%E5%88%AB


def get_file_content(imgdir):
    with open(imgdir, 'rb') as fp:
        return fp.read()


host = 'https://imgurlocr.market.alicloudapi.com'
path = '/urlimages'
method = 'POST'
appcode = '089392f80f954f33bcde1a8ff2e0b747'
querys = ''
bodys = {}
url = host + path

# 1.网络图片识别
# bodys['image'] = '''https://fegine-drug.oss-cn-shanghai.aliyuncs.com/image/urlimage.png'''

# 2.本地图片识别
image_url = './abc.jpg'
image = get_file_content(image_url)
base_image = base64.b64encode(image).decode()
bodys['image'] = 'data:image/jpeg;base64,%s' % base_image



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
if(content):
    print(content.decode('UTF-8'))

