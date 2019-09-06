# a = ['key1','key2','key3','key4']
# b = ['val1','val2','val3','val4']
# d = zip(a,b)
# print(dict(d))

# a = ['a1','a2']
# b = ['b1','b2']
# c = [a,b]
# print(dict(c)) # {'a1': 'a2', 'b1': 'b2'}
# 相当于遍历子列表，如下
# dit = {}
# for i in c:
#     dit[i[0]] = i[1]
# print(dit)

dit = {'name': 'zxf',
       'age': '22',
       'gender': 'male',
       'address': 'shanghai'}

# 将字典的key转换成列表
lst = list(dit)
print(lst)  # ['name', 'age', 'gender', 'address']

# 将字典的value转换成列表
lst2 = list(dit.values())
print(lst2)  # ['zxf', '22', 'male', 'shanghai']
