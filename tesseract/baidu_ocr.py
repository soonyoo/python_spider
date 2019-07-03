from aip import AipOcr


# 参考文档：https://ai.baidu.com/docs#/OCR-Python-SDK/top
# 测试结果：简单的可以，复杂的还是不行，效果没有付费的好
""" 你的 APPID AK SK """
APP_ID = '###'
API_KEY = '###'
SECRET_KEY = '####'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('oa_image.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image)
print(result)
