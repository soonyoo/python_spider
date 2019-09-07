# -*- coding: utf-8 -*-
# from scrapy.exceptions import DropItem
from common.mysql_util import DbPoolUtil

class MySQLPipeline(object):
    """ 把数据保存到MySQL
    批量插入数据到MySQL数据库中
    注意：数据格式:数组(元组)嵌套
    [[字段1的值，字段2的值，字段3的值],[字段1的值，字段2的值，字段3的值],...]
    """
    def __init__(self):
        self.book_list = list()

    def process_item(self,item, spider):
        # 方法一：把字典转成列表(注意字段顺序)
        #item_list = list(item.values())
        # 方法二：元组,指定顺序(建议使用)
        item_list = (item['name'],item['desc'],item['author'],item['pub'],item['pub_date'],item['price'])
        self.book_list.append(item_list)
        return item

    def close_spider(self, spider):
        db_util = DbPoolUtil('mysql')
        # 注mysql中，如果字段名是关键字，需要用`引住，最好不要把字段与关键字冲突，避免不必要的麻烦。
        in_sql = "insert into book_info(`name`,`desc`,author,pub,pub_date,price) values (%s,%s,%s,%s,%s,%s)"
        row_count = db_util.execute_many_iud(in_sql, self.book_list)
        print('成功插入 {} 条记录! '.format(row_count))

