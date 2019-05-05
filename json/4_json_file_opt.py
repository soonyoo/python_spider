# coding = utf-8
import json

"""
author:xuwenyuan
date: 2019-04-30
describe：对json文件操作：
        1.把字符串保存成json文件
        2.读取json文件
        3.Json模块dumps、loads、dump、load函数介绍[后面带s的，与文件有关]
"""


class SaveASJson(object):
    def __init__(self):
        self.persons = [
            {
                'username': "张三",
                'age': 18,
                'country': 'china'
            },
            {
                'username': '李四',
                'age': 20,
                'country': 'china'
            },
            {
                'username': '王五',
                'age': 32,
                'country': 'china'
            }
        ]

        self.persons_dic = {'username': "zhangsan", 'age': 18, 'country': 'china'}
        self.persons_str = 'zhangsan张三'

    @staticmethod
    def save_file(json_string, file_name, coding):
        """
        保存文件函数：把字符串保存成文件
        :param json_string:
        :param file_name:
        :param coding:
        :return:
        """
        with open(file_name, 'w', encoding=coding) as fp:
            fp.write(json_string)

    @staticmethod
    def dump_save_file(json_string, file_name, coding):
        """
        使用dump函数，保存文件
        # json.dump(json_string, fp) 这样写会中文乱码，
        # 如果要保存含有中文的字符串，建议加上ensure_ascii=False,json.dump默认使用ascii字符码

        :param json_string: 要保存的json字符串
        :param file_name: 要保存的文件名称
        :param coding: 字符编码(如utf-8)
        :return: 没有返回值
        """
        with open(file_name, 'w', encoding=coding) as fp:
            json.dump(json_string, fp, ensure_ascii=False)

    @staticmethod
    def read_json_file(file_name, coding):
        """
        使用json.load读取json文件
        :param file_name: 文件名
        :param coding: 编码（如utf-8）
        :return: <class 'list'>
        """
        with open(file_name, 'r', encoding=coding) as fp:
            persons = json.load(fp)
        return persons

    @staticmethod
    def read_file(file_name, coding):
        """
        传统的读取文件方法：详见：https://www.cnblogs.com/zywscq/p/5441145.html
        :param file_name: 文件名称
        :param coding: 编码
        :return: 返回文件内容
        """
        with open(file_name, 'r', encoding=coding) as f:
            content = f.read()
        return content


if __name__ == '__main__':
    save_json = SaveASJson()

    # 这样会中文乱码
    # json_str = json.dumps(save_json.persons_dic)
    # print(type(save_json.persons_dic))
    # print(type(json_str))
    # print(json_str)

    # 这样不会中文乱码
    # json_str = json.dumps(save_json.persons).encode('utf-8').decode('unicode_escape')
    # 调用保存函数
    # SaveASJson.save_file(json_str, 'person.json', 'utf-8')
    # SaveASJson.dump_save_file(save_json.persons, 'person2.json', 'utf-8')
    # 读取json文件
    # person_list = SaveASJson.read_json_file('person2.json', 'utf-8')
    # print(type(person_list))
    # print(person_list)

    # 1.json.dumps()
    # ## 用于将把python对象(dict类型/list类型)的数据转成str(json格式的str)，
    # ## (1).因为如果直接将dict类型/list类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数;
    # ## (2).json.dumps会格式化python对象的代码，转换成jsons标准格式。

    # 1.1 这样会报错
    # SaveASJson.save_file(save_json.persons, 'person.json', 'utf-8')
    # 1.2 先转换，后写入，不会报错
    # persons = json.dumps(save_json.persons, ensure_ascii=False)
    # SaveASJson.save_file(persons, 'person.json', 'utf-8')

    # 2.json.dump()
    # ## json.dump() (1) 用于将dict/list类型的数据转成str，(2) 并写入到json文件中。
    # SaveASJson.dump_save_file(save_json.persons, 'person.json', 'utf-8')

    # 3.json.loads()
    # ## json.loads() 用于将str类型的数据转成dict/list

    tt = SaveASJson.read_file('person.json', 'utf-8')
    print(tt)

    '''
    #
    print(type(save_json.persons))
    # 把python对象（list/dict）转成str (json字符串) 
    persons = json.dumps(save_json.persons)
    print(type(persons))
    persons_list = json.loads(persons)
    print(type(persons_list))
    print(persons_list[0]["username"])

   

    print(type(save_json.persons_str))
    print(save_json.persons_str)
    person_str1 = json.dumps(save_json.persons_str, ensure_ascii=False)
    print(type(person_str1))
    print(person_str1)
    if person_str1 == save_json.persons_str:
        print('true')
    else:
        print('false')

    print(save_json.persons_str[0:5])
    print(person_str1[0:5])
    
    

    '''





