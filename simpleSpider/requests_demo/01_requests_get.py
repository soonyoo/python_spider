# coding: utf-8

import requests


class RequestBaiDu(object):
    """
    requests的get请求
    """

    def parse(self):
        """
        r.status_code #响应状态码
        r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
        r.content #字节(bytes)方式的响应体，会自动为你解码 gzip 和 deflate 压缩
        r.text #字符串(str)方式的响应体，会自动根据响应头部的字符编码进行解码
        r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None

        #特殊方法#
        r.json() #Requests中内置的JSON解码器
        r.raise_for_status() #失败请求(非200响应)抛出异常
        :return:
        """
        # kw = {'wd': 'python'}
        # url = 'https://www.baidu.com/s'
        params = {'query': 'python'}
        url = 'https://www.sogou.com/web'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
        response = requests.get(url=url,params=params, headers=headers)

        # 1. response.text 返回unicode格式数据,会中文乱码,使用response.encoding解决
        # print(type(response.text))
        # 1.1 直指写定encoding:(不推荐，可能仍然乱码，因为不一定是你指定的encoding)
        # response.encoding = 'utf-8'
        # 1.2 获取encoding后，再指定（动态指定，推荐使用），
        # 注意：好像不是这样：如（https://www.12306.cn/mormhweb/）response.encoding为ISO-8859-1，
        # 但还是要写死utf-8才正常显示中文，还是要多测试，多总结
        # encoding = response.encoding
        # print(encoding)
        # response.encoding = encoding
        # print(response.text)

        # 2. response.url：获取请求的url,status_code,headers
        # print(response.url)
        # print(response.status_code)
        # print(response.headers)

        # 3.response.content: 字节(bytes)方式的响应体，会自动为你解码 gzip 和 deflate 压缩
        # 3.1 直接输出的话，会以bytes形式显示
        content = response.content
        # 3.2 decode一下，才会中文显示正常
        # content = response.content.decode('utf-8')
        content = response.content.decode()
        print(content)

        # 4.获取网页的encoding：response.encoding
        # encoding = response.encoding
        # print(encoding)


if __name__ == '__main__':
    baidu = RequestBaiDu()
    baidu.parse()
