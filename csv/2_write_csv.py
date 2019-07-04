# coding = utf-8
import csv

"""
生成csv文件方法：
scrapy框架，参见：D:\python\python_spider\scrapy_demo\xici_spider\xici_spider\pipelines_csv.py
"""


class OptCsv(object):
    @staticmethod
    def write_csv_opt1():
        headers = ['username', 'age', 'height']
        values = [
            ('張三', 18, 180),
            ('李四', 19, 190),
            ('王五', 20, 160)
        ]
        with open('class_room.csv', 'w', encoding='utf-8', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerow(headers)
            writer.writerows(values)

    @staticmethod
    def write_csv_opt2():
        headers = ['username', 'age', 'height']
        values = [
            {'username': '张三', 'age': 18, 'height': 180},
            {'username': '李四', 'age': 19, 'height': 190},
            {'username': '王五', 'age': 20, 'height': 160}
        ]
        with open('class_room1.csv', 'w', encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, headers)
            # 写入表头数据时，需要调用writeheader方法
            writer.writeheader()
            writer.writerows(values)

    @staticmethod
    def write_csv_opt3():
        """
        使用这种方式，保存的数据，用excel直接打开，不会乱码
        :return:
        """
        headers = ['username', 'age', 'height']
        values = [
            {'username': '张三', 'age': 18, 'height': 180},
            {'username': '李四', 'age': 19, 'height': 190},
            {'username': '王五', 'age': 20, 'height': 160}
        ]
        with open('class_room3.csv', 'w', encoding='utf_8_sig', newline='') as fp:
            writer = csv.DictWriter(fp, headers)
            # 写入表头数据时，需要调用writeheader方法
            writer.writeheader()
            writer.writerows(values)


if __name__ == '__main__':
    opt = OptCsv()
    opt.write_csv_opt3()


