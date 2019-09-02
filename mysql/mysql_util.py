# coding=utf-8

import pymysql
import os
import yaml


class MySQLUtil(object):
    def __init__(self):
        config_file_path = os.path.dirname(__file__)
        yaml_file = os.path.join(config_file_path, 'conf.yml')
        self.cols = None
        self.table_name = None
        self.db_charset = 'utf8'
        self.rowcount = 0
        with open(yaml_file, 'r', encoding='utf-8') as fp:
            content = fp.read()
            conf = yaml.load(content, Loader=yaml.FullLoader)  # 用load方法转字典
            # mysql-db
            self.db_url = conf['mysql-db']['db_url']
            self.db_user = conf['mysql-db']['db_user']
            self.db_password = conf['mysql-db']['db_password']
            self.db_name = conf['mysql-db']['db_name']

    def get_version(self):
        """获取mysql的版本信息

        使用 fetchone() 方法获取一条数据

        :return:
        """
        conn = pymysql.connect(self.db_url, self.db_user, self.db_password, self.db_name, charset=self.db_charset)
        cursor = conn.cursor()
        sql = "SELECT VERSION()"
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    def curd_insert(self, table_name, table_columns, parameters, insert_type):
        """插入数据

        :param table_name: 表名称
        :param table_columns: 表的字段名
        :param parameters: 要插入的值
        :param insert_type: 插入类型(单条，批量)
        :return: rowcount 插入的记录数

        数据库操作要谨记防御SQL注入：
        cursor.execute(sql,parameters) 这种写法，
        如：cursor.execute('insert into user (name,password) value (%s,%s)', (name,password))
        千万不要使用拼接字符串
        """
        values = []
        self.cols = ','.join(table_columns).replace('\'', '')

        for i in range(len(table_columns)):
            values.append('%s')
        vals = ','.join(values)
        sql = "insert into %s (%s) values (%s) " % (table_name, self.cols, vals)
        conn = pymysql.connect(self.db_url, self.db_user, self.db_password, self.db_name, charset=self.db_charset)
        cursor = conn.cursor()
        try:
            if insert_type == 1:
                self.rowcount = cursor.execute(sql, parameters)
            else:
                self.rowcount = cursor.executemany(sql, parameters)

            conn.commit()
        except Exception as ex1:
            conn.rollback()
            print(ex1)
        finally:
            conn.close()

        return self.rowcount

    def curd_select(self, table_name, table_columns, condition, parameters):
        """查询数据

        :param table_name: 表名称
        :param table_columns: 表字段
        :param condition: 条件（and user_name = %s ）
        :param parameters: 参数的值，对应条件(condition)中的数值的值，数据类型为数组或元组
        :return: 返回元组列表

        """
        self.cols = ','.join(table_columns).replace('\'', '')
        sql = "select %s from %s where 1=1 %s  " % (self.cols, table_name, condition)
        conn = pymysql.connect(self.db_url, self.db_user, self.db_password, self.db_name, charset=self.db_charset)
        cursor = conn.cursor()
        lists = None
        try:
            cursor.execute(sql, parameters)
            lists = cursor.fetchall()
        except Exception as ex2:
            print(ex2)
        finally:
            cursor.close()
            conn.close()

        return lists

    def curd_delete(self, table_name, condition, parameters):
        """删除测试

        :param table_name: 表名称
        :param condition: 条件
        :param parameters: 条件对应的参数值
        :return: rowcount 影响的行数

        """
        sql = "delete from  %s  where  %s " % (table_name, condition)
        conn = pymysql.connect(self.db_url, self.db_user, self.db_password, self.db_name, charset=self.db_charset)
        cursor = conn.cursor()
        try:
            self.rowcount = cursor.execute(sql, parameters)
            conn.commit()
        except Exception as ex3:
            conn.rollback()
            print(ex3)
        finally:
            cursor.close()
            conn.close()
        return self.rowcount

    def curd_update(self, table_name, set_condition, where_condition, parameters):
        """ 更新数据

        :param table_name: 表名称
        :param set_condition: set的条件
        :param where_condition: where的条件
        :param parameters: 对应set条件的值
        :return:
        """
        sql = "UPDATE %s SET %s WHERE %s " % (table_name, set_condition, where_condition)
        conn = pymysql.connect(self.db_url, self.db_user, self.db_password, self.db_name, charset=self.db_charset)
        cursor = conn.cursor()
        try:
            self.rowcount = cursor.execute(sql, parameters)
            conn.commit()
        except Exception as ex4:
            conn.rollback()
            print(ex4)
        finally:
            cursor.close()
            conn.close()
        return self.rowcount
