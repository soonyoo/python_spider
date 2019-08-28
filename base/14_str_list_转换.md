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



