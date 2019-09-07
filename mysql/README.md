# python 读写mysql数据库

> 一定要注意：防止SQL注入的写法

## 1.防注入
```
# 注意数据库操作要使用：
# 1.1 错误用法 
#不要使用以下这种写法，这种写法是直接将参数拼接到sql语句中，这样数据库就容易被sql注入攻击：
cursor.execute(sql) # sql 使用拼接字符串，如下：
cursor.execute("select * from user where user='%s' and password='%s' " % (name,password))
# 1.2 正确用法 
cursor.execute(sql,args) # sql,args参数这种模式: 其中args为元组或数组类型,如下面写法
cursor.execute('insert into user (name,password) value (%s,%s)',(name,password))
```

## 2.读配置文件conf.yml
>详见代码：mysql_util.py


## 3. DBUtils 
> 以上的方法(mysql_util.py)不推荐，原因是没有使用数据库连接池

参考文章：  
- python DbUtils 使用教程  
https://blog.csdn.net/jacke121/article/details/79852146  

- python使用DBUtils连接部分主流数据库  
https://blog.csdn.net/danengbinggan33/article/details/80667204


### 3.1 安装DBUtils
```bash
pip install DBUtils
```
### 3.2 DB-API 2规范的相关数据库连接模块
```bash
pip install pymysql（mysql）
pip install pymssql（sqlserver）
pip install cx_Oracle（oracle）
pip install phoenixdb（hbase）
pip install sqlite3（sqlite3 python自带）
```
### 3.3 详见mysql_pool_util.py

### 3.4 python scrapy框架通过pipelines批量存储万条数据到mysql数据库
```python
# -*- coding: utf-8 -*-
#!DATE: 2018/7/15 13:26
#!@Author: yy
import sys
import MySQLdb

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class CncompanyidSpiderFastPipeline(object):
    companylist = []

    def open_spider(self, spider):
        self.conn = MySQLdb.connect(host="***", user="***", passwd="***",db="***",charset="utf8")
        self.cursor = self.conn.cursor()
        # 存入数据之前清空表：
        self.cursor.execute("truncate table cn_companyid")
        self.conn.commit()

    # 批量插入mysql数据库
    def bulk_insert_to_mysql(self, bulkdata):
        try:
            print "the length of the data-------", len(self.companylist)
            sql = "insert into cn_companyid (id, name) values(%s, %s)"
            self.cursor.executemany(sql, bulkdata)
            self.conn.commit()
        except:
            self.conn.rollback()

    def process_item(self, item, spider):
        self.companylist.append([item['CompanyID'], item['Companyname']])
        if len(self.companylist) == 1000:
            self.bulk_insert_to_mysql(self.companylist)
            # 清空缓冲区
            del self.companylist[:]
        return item

    def close_spider(self, spider):
        print "closing spider,last commit", len(self.companylist)
        self.bulk_insert_to_mysql(self.companylist)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
```

