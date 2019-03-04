# coding = utf-8

from pymongo import MongoClient
import pymongo

# from pymongo.cursor.Cursor


class MongoDBOpt:

    # 数据库连接初始化
    def __init__(self):
        self.ip = 'localhost'
        # 端口为int类型
        self.port = 27017
        self.conn = MongoClient(self.ip, self.port)
        self.db = self.conn.spider_db
        self.dataset = self.db.qsbk

    # 插入单条数据
    def insert(self, dic):
        return self.dataset.insert(dic)

    # 插入多条数据
    def insert_many(self, list_dic):
        return self.dataset.insert_many(list_dic)

    # 查询数据,返回一条数据(返回字典类型:<class 'dict'>)
    def search_one(self, dic):
        return self.dataset.find_one(dic)

    # 查询多条数据(返回数据类型：<class 'pymongo.cursor.Cursor'>  iterator )
    def search(self, dic):
        return self.dataset.find(dic)

    # 计数 count
    def count(self,dic=None):
        return self.dataset.find(dic).count()

    # 排序 sort
    def sort(self, order_field, dic=None):
        return self.dataset.find(dic).sort(order_field, pymongo.ASCENDING)

    # 偏移skip
    def skip(self, order_field, step, dic=None):
        # stop为2时只取第三个及后面的元素
        results = self.dataset.find(dic).sort(order_field, pymongo.ASCENDING).skip(step)
        return results

    # 定要取的结果个数 limit
    # 注：skip,sort,limit 顺序不限制。
    # results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)  # 只取两个结果

    # 更新
    # 1 更新一条记录
    def update_one(self, condition_field, set_content):
        return self.dataset.update_one(condition_field, set_content)
    # {'$set': {'age': 12}}

    # 2 更新多条记录
    '''
    # updata_many()会将所有符合条件的数据都更新
    result = collection.update_many({'date': {'$gt': 2}}, {'$inc': {'data': 10}})  # 将所有date值大于2的文档加上10
    '''
    def update_many(self, condition_field, set_content):
        return self.dataset.update_many(condition_field, set_content)

    # 删除
    # 1 删除一条记录
    def delete_one(self, condition_dict):
        return self.dataset.delete_one(condition_dict)

    # 2 删除多条记录
    def delete_many(self, condition_dict):
        return self.dataset.delete_many(condition_dict)


if __name__ == '__main__':
    mongodb = MongoDBOpt()

    # 添加单条数据
    # info1 = {"author": "zhangsan", "content": "abc"}
    # result = mongodb.insert(info1)
    # print(result)
    #
    # info1 = {"author": "react", "content": "cde"}
    # result = mongodb.insert(info1)
    # print(result)

    # 添加多条数据到集合中
    # info1 = [{"name": "zhangsan", "age": 28}, {"name": "lisi", "age": 23}]
    # mongodb.insert_many(info1)

    # opt = {'name': 'zhangsan'}

    # 名字为zhangsan并且age>20
    # opt = {'age':{'$gt':20},'name':'zhangsan'}

    # 读取单条数据
    # result = mongodb.search_one(opt)
    # print(type(result))
    # print(result)

    # 读取多条数据
    # lists = mongodb.search(opt)
    # for li in lists:
    #     print(li)

    # 计数
    # 加条件
    # result = mongodb.count(opt)
    # 不加条件
    # result = mongodb.count()
    # print(result)

    # 排序
    # lists = mongodb.sort('age', opt)
    # lists = mongodb.sort('age')
    # for li in lists:
    #     print(li)

    # 偏移
    # 跳过前面2行数据,从第5行开始
    # lists = mongodb.skip('age', 5)
    # for li in lists:
    #     print(li)

    # 定要取的结果个数
    # 只取两个结果

    # lists = mongodb.dataset.find().limit(6).skip(2).sort('age')
    # for li in lists:
    #     print(li)

    # 更新
    # 1.更新一条记录
    # 将 name= 'zhangsan', age = 28的数据，把字段age,改为38
    # condition_dict = {'name': 'zhangsan', 'age': 28}
    # update_content = {'$set': {'age': 38}}
    # result = mongodb.update_one(condition_dict,update_content)
    # print(result)
    # print(result.matched_count, result.modified_count)  # 打印匹配的数据条数和影响的数据条数

    # 2.更新多条记录
    # 将 name= 'zhangsan'的数据，把字段age,改为18
    # condition_dict = {'name': 'zhangsan'}
    # update_content = {'$set': {'age': 18}}
    # result = mongodb.update_many(condition_dict,update_content)
    # print(result)
    # print(result.matched_count, result.modified_count)  # 打印匹配的数据条数和影响的数据条数

    # 删除
    # 1 删除一条记录
    # '''
    result = mongodb.delete_one({"author": "react"})
    print(result)
    # print(result.raw_result)
    # print(result.deleted_count)
    # '''
    # {'n': 1, 'ok': 1.0}
    #     1
    # 2 删除多条记录
    # result = mongodb.delete_many({'name': 'react'})
    # print(result)
    # print(result.raw_result)
    # print(result.deleted_count)
    # {'n': 5, 'ok': 1.0}
    # 5








