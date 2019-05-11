# coding = utf-8
from pymongo import MongoClient


class DBUtil(object):
    def __init__(self, tb_name):
        self.ip = 'localhost'
        # 端口为int类型
        self.port = 27017
        self.conn = MongoClient(self.ip, self.port)
        self.db = self.conn.spider_db
        # 下面方法不行：命令行才有createCollection
        # self.db.createCollection(tb_name)
        # 用此方法创建集合(动态创建集合/表的方法)
        self.dataset = self.db[tb_name]

    # 批量插入数据库
    def insert_many_db(self, list_dic):
        self.dataset.insert_many(list_dic)


if __name__ == '__main__':
    print("are you ok?")
    # 这样不会创建集合，当有插入等操作时才会创建。
    # dbUtil = DBUtil('movie')


