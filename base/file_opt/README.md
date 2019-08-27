# python对文件的操作

## 1.文件目录操作

### 1.1 获取文件当前所在的路径
```python
current_path = os.path.dirname(__file__)
```
### 1.2 获取当前文件所在的路径的上级目录
```python
pre_path = os.path.dirname(current_path)
```
### 1.3 拼接路径
```python
images_path = os.path.join(pre_path,'images')
```
### 1.4 创建目录
```python
    # 如果目录不存在，创建目录
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    else:
        print('目录已存在...')
```
## 2. 文件名修改
### 2.1 方法一：os.rename
>
src – 要修改的目录名
dst – 修改后的目录名
```python
os.rename(src, dst)参数
```
### 2.2 方法二：shutil.move
>src - 原来的文件全路径(含文件名)
dst - 修改后的文件全路径(含文件名)
```python
shutil.move(src, dst)
```

## 3.python 中使用 shutil 实现文件或目录的复制、删除、移动
参见：https://blog.csdn.net/qq_38640439/article/details/81410116



