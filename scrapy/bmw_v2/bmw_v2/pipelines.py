# -*- coding: utf-8 -*-
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from bmw_v2 import settings


class BmwV2Pipeline(object):
    def __init__(self):
        # 当前文件上级目录的images文件夹，如果不存在，创建。
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    # 使用images pipelines后，下面这个方法没用了。
    def process_item(self, item, spider):
        category = item["category"]
        image_urls = item["image_urls"]
        # 文件夹，根据category来创建
        category_path = os.path.join(self.path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for image_url in image_urls:
            image_name = image_url.split('_')[-1]
            request.urlretrieve(image_url,os.path.join(category_path, image_name))
        return item


class BMWImagePipeline(ImagesPipeline):
    # 重写get_media_requests方法
    def get_media_requests(self, item, info):
        # 这个方法是在发送下载请求之前调用；
        # 其实这个方法本身就是去发送下载请求的。
        request_objs = super(BMWImagePipeline, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    # 重写file_path方法
    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        path = super(BMWImagePipeline, self).file_path(request,response,info)
        category = request.item.get('category')
        image_store = settings.IMAGES_STORE
        category_path = os.path.join(image_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace("full/", "")
        image_path = os.path.join(category_path,image_name)
        return image_path
