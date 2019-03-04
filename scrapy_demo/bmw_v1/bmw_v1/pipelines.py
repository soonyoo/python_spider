# -*- coding: utf-8 -*-
import os
from urllib import request


class BmwV1Pipeline(object):
    def __init__(self):
        # 当前文件上级目录的images文件夹，如果不存在，创建。
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

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
