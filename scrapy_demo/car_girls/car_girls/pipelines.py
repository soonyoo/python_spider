# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
import os
from car_girls import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CarGirlsImagesPipeline(ImagesPipeline):
    # 重写get_media_requests方法
    def get_media_requests(self, item, info):
        # 这个方法是在发送下载请求之前调用；
        # 其实这个方法本身就是去发送下载请求的。
        request_objs = super(CarGirlsImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    # 重写file_path方法
    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        path = super(CarGirlsImagesPipeline, self).file_path(request, response, info)
        brand = request.item.get('brand')
        images_num = request.item.get('images_num')
        girls_name = request.item.get('girls_name')
        images_store = settings.IMAGES_STORE

        # 注意不要使用拼字符串，使用os.path.join
        if not os.path.exists(images_store):
            os.mkdir(images_store)

        brand_path = os.path.join(images_store,brand+images_num)
        if not os.path.exists(brand_path):
            os.mkdir(brand_path)

        girls_path = os.path.join(brand_path, girls_name)
        if not os.path.exists(girls_path):
            os.mkdir(girls_path)

        # image_name = path.replace("full/", "")
        image_name = path.rsplit('/')[-1]
        image_path = os.path.join(girls_path, image_name)
        # print('-'*30)
        # print(image_path)
        return image_path
