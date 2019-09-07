# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from car_beauty import settings

class CarBeautyPipeline(object):
    def __init__(self):
        # 设置默认存放目录1
        self.base_path ='D:/python/car_mm_photo'
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)

    def process_item(self, item, spider):
        car_type = item['brand']
        photo_num = item['num']
        mm_name = item['title']
        img_url = item['img_url']
        img_name = img_url.split('/')[-1]

        # 车类型目录2
        car_type_path = self.base_path + '/' + car_type + photo_num
        if not os.path.exists(car_type_path):
            os.mkdir(car_type_path)
        # 美女目录3
        full_path = car_type_path + '/' + mm_name
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        # 开始下载
        try:
            request.urlretrieve(img_url, os.path.join(full_path, img_name))
        except Exception as ex:
            print(ex)
        return item
