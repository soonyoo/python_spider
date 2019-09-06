# coding = utf-8
"""
@author: xuwenyuan
date: 2019-09-05
desc: csv操作工具类
"""
import csv
import os

class CsvUtil(object):
    @staticmethod
    def create_csv_file(csv_header, values,file_full_path,check_exist=False):
        """创建CSV文件方法

        :param csv_header: 字段的名称，数组格式
        :param values: csv的内容，数组+字典格式
        :param file_full_path: csv文件的全路径，
               1.如果目录不存在，创建目录(支持多级目录创建);
               2.目录格式用反斜杠'D:/python/2019-09-05/ok/1.csv',不能用\或\\表示;
        :param check_exist: 检查文件是否存在,
               1.如果check_exist=False,覆盖原来的文件；
               2.如果check_exist=True,提示文件已存在，不做处理。
        :return:
        """
        if os.path.exists(file_full_path) and check_exist:
            print('Documents already exist...')
        else:
            dir = file_full_path.rsplit('/', 1)[0]
            if not os.path.exists(dir):
                os.makedirs(dir, exist_ok=True)
            with open(file_full_path, 'w', encoding='utf_8_sig', newline='') as fp:
                writer = csv.DictWriter(fp, csv_header)
                writer.writeheader()
                writer.writerows(values)

if __name__ == '__main__':
    file_full_path = 'D:/python/2019-09-05/ok/1.csv'
    headers = ['username', 'age', 'height']
    values = [
        {'username': '张三', 'age': 18, 'height': 180},
        {'username': '李四', 'age': 19, 'height': 190},
        {'username': '王五', 'age': 20, 'height': 160}
    ]
    CsvUtil.create_csv_file(headers,values,file_full_path,check_exist=False)
