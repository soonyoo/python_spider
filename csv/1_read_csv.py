# coding = utf-8

import csv
# from collections import Iterable
import copy

"""
操作CSV文件：csv文件读取，带表头，不带表头，转为字典
"""


class OptCsvFile(object):
    def __init__(self):
        self.csv_lis = []

    @staticmethod
    def read_csv_list(file_name):
        """
        直接读取csv文件的全部内容，包括表头
        :param file_name: 文件名称
        :return: 返回数据列表
        """
        with open(file_name, 'r') as fp:
            # reader 是一个迭代器
            reader = csv.reader(fp)
            line_list = list(map(lambda line_text: line_text, reader))
            # 作用与下面三行相同：
            # line_list = []
            # for line_text in reader:
            #     line_list.append(line_text)
        return line_list

    @staticmethod
    def read_csv_data_list(file_name):
        """
        读取csv文件，跳过表头一行
        :param file_name: 文件名称
        :return: 返回数据列表
        """
        with open(file_name, 'r') as fp:
            # reader 是一个迭代器
            reader = csv.reader(fp)
            # 如果不要第一行，可以用next
            next(reader)
            line_list = list(map(lambda line_text: line_text, reader))
        return line_list

    @staticmethod
    def read_csv_dict_data(file_name):
        with open(file_name, 'r') as fp:
            reader = csv.DictReader(fp)
            line_list = list(map(lambda line_text: line_text, reader))
        return line_list


if __name__ == '__main__':
    opt = OptCsvFile()
    lis = opt.read_csv_list('stock.csv')
    # lis = opt.read_csv_data_list('stock.csv')
    for x in lis:
        print(x)


    # lis = opt.read_csv_dict_data('stock.csv')
    # print(type(lis))
    # for x in lis:
    #     values = {'name': x["secShortName"], 'volumn': x['turnoverVol']}
    #     print(values)
