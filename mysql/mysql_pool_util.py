# -*- coding:utf-8 -*-

""" DBUtils

Description: DB工具类
@author: xuwenyuan
@date: 2019-09-02
"""
from DBUtils.PooledDB import PooledDB
import yaml
import os
import importlib
import uuid
import datetime
import time


class DbPoolUtil(object):

    __DBConfig = dict()

    def __init__(self, db_type):
        self.__db_type = db_type
        self.__DBConfig = self.read_yaml('conf.yml')
        if self.__db_type == "mysql":
            config = {
                'host': self.__DBConfig['db_url'],
                'port': self.__DBConfig['db_port'],
                'database': self.__DBConfig['db_name'],
                'user': self.__DBConfig['db_user'],
                'password': self.__DBConfig['db_password'],
                'charset': self.__DBConfig['db_charset']
            }
            db_creator = importlib.import_module("pymysql")
            """PooledDB
            :param creator: 使用连接数据库的模块(mysql,sqlserver,oracle,hbase)
            :param mincached: 初始化时，连接池中至少创建的空闲的连接，0表示不创建
            :param maxcached: 连接池中最多闲置的连接，0和NONE不限制，
            :param maxshared: 连接池中最多共享连接数量， 0和NONE表示全部共享，PS:无用,
                              因为pymysql和mysqldb的模块的threadsafety都为1，所有制无论设置为多少，
                              maxcached永远为0，所以永远是所有连接都共享。
            :param maxconnections: 连接池允许的最大连接数(0和NONE表示不限制)
            :param blocking: 连接池中如果没有可用连接后，是否阻塞等待，True，等待，False 不等待
            :param maxusage: 一个连接最多被重复使用的次数，None表示无限制
            :param setsession: 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            :param reset: how connections should be reset when returned to the pool
                        (False or None to rollback transcations started with begin(),
                        True to always issue a rollback for safety's sake)
            :param failures: an optional exception class or a tuple of exception classes
                        for which the connection failover mechanism shall be applied,
                        if the default (OperationalError, InternalError) is not adequate
            :param ping: ping MySQL服务端，检查是否服务可用。0 = None = never,1 = default = whenever it is requested, 2 = when a cursor is created,
            """
            self.__pool = PooledDB(db_creator, maxcached=50, maxconnections=100, blocking=True, maxusage=None, **config)

    def read_yaml(self, file_name):
        config_file_path = os.path.dirname(__file__)
        yaml_file = os.path.join(config_file_path, file_name)
        with open(yaml_file, 'r', encoding='utf-8') as fp:
            content = fp.read()
            conf = yaml.load(content, Loader=yaml.FullLoader)  # 用load方法转字典
            # mysql-db
            self.__DBConfig['db_url'] = conf['mysql-db']['db_url']
            self.__DBConfig['db_user'] = conf['mysql-db']['db_user']
            self.__DBConfig['db_password'] = conf['mysql-db']['db_password']
            self.__DBConfig['db_name'] = conf['mysql-db']['db_name']
            self.__DBConfig['db_charset'] = conf['mysql-db']['db_charset']
            self.__DBConfig['db_port'] = conf['mysql-db']['db_port']
        return self.__DBConfig

    def execute_query(self, sql, dict_mark=False, args=()):
        """
        执行查询语句，获取结果
        :param sql:sql语句，注意防注入
        :param dict_mark:是否以字典形式返回，默认为False
        :param args:传入参数
        :return:结果集
        """
        result = []
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            if dict_mark:
                cur.execute(sql, args)
                # name为description的第一个内容，表示为字段名
                fields = [desc[0] for desc in cur.description]
                rst = cur.fetchall()
                if rst:
                    result = [dict(zip(fields, row)) for row in rst]
            else:
                cur.execute(sql, args)
                result = cur.fetchall()
        except Exception as e:
            print('异常信息:' + str(e))
        finally:
            cur.close()
            conn.close()
        return result

    def execute_query_single(self, sql, dict_mark=False, args=()):
        """
        执行查询语句，获取单行结果
        :param sql:sql语句，注意防注入
        :param dict_mark:是否以字典形式返回，默认为False
        :param args:传入参数
        :return:结果集
        """
        result = []
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            if dict_mark:
                cur.execute(sql, args)
                # name为description的第一个内容，表示为字段名
                fields = [desc[0] for desc in cur.description]
                rst = cur.fetchone()
                if rst:
                    result = dict(zip(fields, rst))
            else:
                cur.execute(sql, args)
                result = cur.fetchone()
        except Exception as e:
            print('异常信息:' + str(e))
        cur.close()
        conn.close()
        return result

    def execute_iud(self, sql, args=()):
        """
        执行增删改语句
        :param sql:sql语句，注意防注入
        :param args:传入参数
        :return:影响行数,mysql和sqlite有返回值
        """
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        try:
            result = cur.execute(sql, args)
            conn.commit()
            if self.__db_type == "mysql":
                count = result
            if self.__db_type == "sqlite3":
                count = result.rowcount
        except Exception as e:
            print('execute_iud 异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count

    def execute_many_iud(self, sql, args):
        """
        批量执行增删改语句
        :param sql:sql语句，注意防注入
        :param args:参数,内部元组或列表大小与sql语句中参数数量一致
        :return:影响行数，mysql和sqlite有返回值
        """
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        loopK = 5000
        try:
            k = len(args)
            if k > loopK:
                n = k // loopK
                for i in range(n):
                    arg = args[(i * loopK): ((i + 1) * loopK)]
                    cur.executemany(sql, arg)
                    conn.commit()
                arg = args[(n * loopK):]
                if len(arg) > 0:
                    cur.executemany(sql, arg)
                    conn.commit()
            else:
                result = cur.executemany(sql, args)
                conn.commit()
                if self.__db_type == "mysql":
                    count = result
                if self.__db_type == "sqlite3":
                    count = result.rowcount
        except Exception as e:
            print('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count

    def execute_proc(self, proc_name, args=()):
        """
        执行存储过程，mysql适用
        :param proc_name:存储过程/函数名
        :param args:参数
        :return:result为结果集，args_out为参数最终结果（用于out，顺序与传参一致）
        """
        result = ()
        args_out = ()
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            cur.callproc(proc_name, args)
            result = cur.fetchall()
            if args:
                sql = "select " + ",".join(["_".join(["@", proc_name, str(index)]) for index in range(len(args))])
                cur.execute(sql)
                args_out = cur.fetchone()
            conn.commit()
        except Exception as e:
            print('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return result, args_out

    def loop_row(self, obj, fun_name, sql, args=()):
        """
        执行查询语句，并且对游标每行结果反射调用某个处理方法
        主要是考虑一些表记录太大时，不能一次性取出,游标式取数据
        :param obj: 对象或者模块
        :param fun_name:调用方法名
        :param sql:sql语句，注意防注入
        :param args:传入参数
        :return:
        """
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args)
            fun = getattr(obj, fun_name)
            while True:
                row = cur.fetchone()
                if row is None:
                    break
                fun(row)
        except Exception as e:
            print('异常信息:' + str(e))
        cur.close()
        conn.close()

    def loop_row_custom(self, sql, args=()):
        """
        执行查询语句，并且对游标每行结果执行某些操作或者直接返回生成器
        主要是考虑一些表记录太大时，不能一次性取出,游标式取数据
        :param sql:sql语句，注意防注入
        :param args:传入参数
        :return:
        """
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args)
            while True:
                row = cur.fetchone()
                if row is None:
                    break
                # 在此编写你想做的操作
                print(row)
        except Exception as e:
            print('异常信息:' + str(e))
        cur.close()
        conn.close()


if __name__ == '__main__':
    db_util = DbPoolUtil('mysql')

    """ 1.1 查询返回多条记录
    1.1 execute_query 的使用；
    1.2 元组中只包含一个元素时，需要在元素后面添加逗号：
        in_args = ('小王1',)
    
    """
    # in_args = ('小李',)
    # in_sql = "select * from employee where user_name = %s"
    # lists = db_util.execute_query(in_sql, False, in_args)
    # for lis in lists:
    #     print(lis)

    """1.2 查询单条记录
    
    execute_query_single
    
    """
    # in_args = ('小李',)
    # in_sql = "select * from employee where user_name = %s"
    # lists = db_util.execute_query_single(in_sql, False, in_args)
    # print(lists)

    """2.1 插入记录测试
    单条记录插入
    execute_iud(self, sql, args=()):
    """
    # in_sql = "insert into employee(id, user_name, age, email, gender, income) values (%s,%s,%s,%s,%s,%s)"
    # in_args = (str(uuid.uuid1()), '老王8', 88, 'laowang8@chinaunicom.cn', 1, 1000)
    # row_count = db_util.execute_iud(in_sql, in_args)
    # print('成功插入 {} 条记录! '.format(row_count))

    """2.1 插入记录测试
    多条记录一起插入
    execute_many_iud
    """
    value_list = list()
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    value_list.append([str(uuid.uuid1()), 'zhangsan', 18, 'zhangsan@chinaunicom.cn', 0, 7000, nowTime])
    time.sleep(0.1)
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    value_list.append([str(uuid.uuid1()), 'lishi', 22, 'lishi@chinaunicom.cn', 1, 4000, nowTime])
    time.sleep(0.1)
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    value_list.append([str(uuid.uuid1()), 'wangwu', 68, 'wangwu@chinaunicom.cn', 0, 3200, nowTime])

    in_sql = "insert into employee(id, user_name, age, email, gender, income,create_date) values (%s,%s,%s,%s,%s,%s,%s)"
    row_count = db_util.execute_many_iud(in_sql, value_list)
    print('成功插入 {} 条记录! '.format(row_count))







