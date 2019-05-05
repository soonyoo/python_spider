# coding = utf-8

import json

"""
json.loads 使用：
把json字符串(str)转换成python对象dict/list
"""


class Json2Dict(object):
    @staticmethod
    def json_loads(json_str):
        return json.loads(json_str)


if __name__ == '__main__':
    persons_list = "[{\"username\": \"zhangsan\", \"age\": 18, \"country\": \"china\"}, {\"username\": \"lishi\", \"age\": 20, \"country\": \"china\"}]"
    dict_list = Json2Dict.json_loads(persons_list)
    print(type(dict_list))
    print(dict_list[0]["username"])
    print('*' * 30)

    persons_dict_str = "{\"username\": \"zhangsan\", \"age\": \"18\",\"country\": \"china\"}"
    persons_dict = Json2Dict.json_loads(persons_dict_str)
    print(type(persons_dict))
    print(persons_dict["age"])
#
