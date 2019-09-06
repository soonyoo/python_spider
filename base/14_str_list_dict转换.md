# Python list 和 str 互转
## 1. list转字符串
命令：
```python
''.join(list)
```
>其中，引号中是字符之间的分割符，如 空格，“,”，“;”，“\t” 等等
如：
```python
list1 = [1, 2, 3, 4, 5]
''.join(list1)  # 结果即为：12345
','.join(list1) # 结果即为：1,2,3,4,5
```
## 2. 字符串转list

### 2.1 使用list强转
```python
print(list('12345'))

# 输出： ['1', '2', '3', '4', '5']

print (list(map(int, '12345')))

# 输出： [1, 2, 3, 4, 5]
```
### 2.2 使用split
```python
str2 = "123 sjhid dhi" 
list2 = str2.split() # or list2 = str2.split(" ") 
print(list2) 

# 输出：['123', 'sjhid', 'dhi']

str3 = "www.google.com" 
list3 = str3.split(".") 
print(list3)

# 输出： ['www', 'google', 'com']
```
### 3 python列表和字典之间的相互转换
#### 3.1 列表转换成字典
注：列表不能直接使用dict转换成字典。  
##### 3.1.1 方法一：使用zip()函数
```python
a = ['key1','key2','key3','key4']
b = ['val1','val2','val3','val4']
d = zip(a,b)
print(dict(d))
```
>out put:  
>{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}

将a和b两个列表内的元素两两组合成键值对。  
当两个列表的长度不一致时，多出的元素在另一个列表无匹配的元素时就不展示多出的元素。
```python
a = ['key1','key2','key3','key4']
b = ['val1','val2','val3']
d = zip(a,b)
print(dict(d))
```
>out put:  
>{'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
##### 3.1.2 方法二：使用嵌套列表转换为字典
```python
a = ['a1','a2']
b = ['b1','b2']
c = [a,b]
print(dict(c)) # {'a1': 'a2', 'b1': 'b2'}
# 相当于遍历子列表，如下
dit = {}
for i in c:
    dit[i[0]] = i[1]
print(dit)
```
a和b列表内只能有两个元素，将列表内的元素自行组合成键值对。

####3.2 字典转换成列表
注：字典可以直接使用list转换成列表。  
```python

dit = {'name':'zxf',
       'age':'22',
       'gender':'male',
       'address':'shanghai'}
 
# 将字典的key转换成列表
lst = list(dit)
print(lst)  # ['name', 'age', 'gender', 'address']
 
# 将字典的value转换成列表
lst2 = list(dit.values())
print(lst2)  # ['zxf', '22', 'male', 'shanghai']

```


