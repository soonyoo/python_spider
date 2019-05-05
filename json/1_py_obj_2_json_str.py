# coding = utf-8
import json
"""
把python对象dict/list转换为json字符串
"""
persons = [
    {
        'username': "zhangsan",
        'age': 18,
        'country': 'china'
    },
    {
        'username': 'lishi',
        'age': 20,
        'country': 'china'
    }
]
# 把python对象转换为json字符串
json_str = json.dumps(persons)
print(json_str)

