import json

"""
有些函数使用忘记了，在这里测试
"""

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


if __name__ == '__main__':
    # movie_lists = read_json_file('unicom_oa_data.json', 'utf-8')
    # for lis in movie_lists:
    #     print(lis['url'])
    url = "http://wsxy.chinaunicom.cn/api/learner/offering-courses/35535"
    class_id = url.split("/")[-1]
    print(class_id)


