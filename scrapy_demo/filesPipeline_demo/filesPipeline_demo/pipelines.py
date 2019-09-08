# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from filesPipeline_demo import settings
import os


class FilespipelineDemoPipeline(object):
    def process_item(self, item, spider):
        return item


class FilesPipelineTwisted(FilesPipeline):
    # 重写get_media_requests方法
    def get_media_requests(self, item, info):
        # 这个方法是在发送下载请求之前调用；
        # 其实这个方法本身就是去发送下载请求的。
        request_objs = super(FilesPipelineTwisted, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    # 重写file_path方法
    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        path = super(FilesPipelineTwisted, self).file_path(request, response, info)
        # file_urls = request.item.get('file_urls')
        files_store = settings.FILES_STORE
        file_name = request.item.get('file_name')
        # print('get_name:' + get_name)

        if not os.path.exists(files_store):
            os.makedirs(files_store)

        # 默认文件路径"full/xxx.jpg"
        # image_name = path.replace("full/", "")
        # file_name = path.rsplit('/', 1)[-1]
        file_path = os.path.join(files_store, file_name)
        return file_path
