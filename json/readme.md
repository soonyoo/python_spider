# json 操作相关

## 把python对象转换为json字符串
```python
import  json
persons = [
    {
        'username':"zhangsan",
        'age': 18,
        'country': 'china'
    },
    {
        'username': 'lishi',
        'age': 20,
        'country': 'china'
    }
]
# 使用 json.dumps
json_str = json.dumps(persons)
print(json_str)
# 结果
[{"country": "china", "username": "zhangsan", "age": 18}, {"country": "china", "username": "lishi", "age": 20}]

```
>详见例子：1_python_str_2_json.py



## 把python对象转换为json字符串,中文字符乱码处理

```python
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
```

>参见 2_python_str_2_json_chs.py

## 把字符串保存成json文件
> 重点了解json.dumps(),json.loads(),json.dump(),json.load()几个函数的用法。
```python
# coding = utf-8
import json

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
            }
        ]

    @staticmethod
    def save_file(json_string, file_name, coding):
        with open(file_name, 'w', encoding=coding) as fp:
            fp.write(json_string)


if __name__ == '__main__':
    save_json = SaveASJson()

    # 这样会中文乱码
    # json_str = json.dumps(save_json.persons)

    # 这样不会中文乱码
    json_str = json.dumps(save_json.persons).encode('utf-8').decode('unicode_escape')
    # 调用保存函数
    SaveASJson.save_file(json_str, 'person.json', 'utf-8')
```
> 参见3_str_2_json_file.py

