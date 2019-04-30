# coding = utf-8
import json
# 将python对象转换为json字符串
persons = [
    {
        'username': "张三",
        'age': 18,
        'country': 'china'
    },
    {
        'username': '李四',
        'age': 20,
        'country': 'china'
    }
]
# 使用普通方式处理
json_str = json.dumps(persons)
print(json_str)
# [{"country": "china", "username": "\u5f20\u4e09", "age": 18}, {"country": "china", "username": "\u674e\u56db", "age": 20}]

# 先encode,再decode
json_str_chs = json.dumps(persons).encode('utf-8').decode('unicode_escape')
print(json_str_chs)
# [{"username": "张三", "country": "china", "age": 18}, {"username": "李四", "country": "china", "age": 20}]
