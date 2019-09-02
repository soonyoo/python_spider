# coding=utf-8

import mysql_util
import uuid


# def test(aa):
#     if aa == 1:
#         print(1)

if __name__ == '__main__':
    util = mysql_util.MySQLUtil()

    """测试插入
    
    1.1 单个插入
    
    """
    # table_name = 'employee'
    # cols = ['id', 'user_name', 'age', 'email', 'gender', 'income']
    # vals = (str(uuid.uuid1()), '老王', 58, 'laowang@chinaunicom.cn', 1, 18000)
    # row_count = util.curd_insert(table_name, cols, vals, 1)
    # print('成功插入 {} 条记录! '.format(row_count))

    # 1.2 批量插入
    # table_name = 'employee'
    # cols = ['id', 'user_name', 'age', 'email', 'gender', 'income']
    # value_list = list()
    # value_list.append([str(uuid.uuid1()), 'zhangsan', 18, 'zhangsan@chinaunicom.cn', 0, 7000])
    # value_list.append([str(uuid.uuid1()), 'lishi', 22, 'lishi@chinaunicom.cn', 1, 4000])
    # value_list.append([str(uuid.uuid1()), 'wangwu', 68, 'wangwu@chinaunicom.cn', 0, 3200])
    # row_count = util.curd_insert(table_name, cols, value_list, 2)
    # print('成功插入 {} 条记录! '.format(row_count))


    #
    """2.查询测试
    
    condition = ' and user_name = %s '
    %s 不需要加单引（'%s'），因为此处相当于使用参数绑定（防注入的模式，而不是拼字符串）
    
    """
    # table_name = 'employee'
    # cols = ['id', 'user_name', 'age', 'email', 'gender', 'income']
    # condition = ' and user_name = %s '
    # params = ['小李']
    #
    # list1 = util.curd_select(table_name, cols, condition, params)
    # for lis in list1:
    #     print(lis)

    """3.删除测试
    
    """
    # table_name = 'employee'
    # condition = ' user_name = %s '
    # params = ['老王']
    # row_count = util.curd_delete(table_name, condition, params)
    # print('成功删除 {} 条记录! '.format(row_count))

    """4.update 测试
    """
    table_name = 'employee'
    set_condition = ' user_name = %s, age = %s '
    where_codition = ' id = %s '
    params = ['zhangsan', 29, '240c2e24-cd58-11e9-9568-8c1645e715ad']
    row_count = util.curd_update(table_name, set_condition, where_codition, params)
    print('成功更新 {} 条记录! '.format(row_count))












