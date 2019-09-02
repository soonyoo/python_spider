# python 读写mysql数据库

> 一定要注意：防止SQL注入的写法

## 1.防注入
```python
#注意数据库操作要使用：
cursor.execute('insert into user (name,password) value (%s,%s)',(name,password))
 
#不要使用以下这种写法，这种写法是直接将参数拼接到sql语句中，这样数据库就容易被sql注入攻击：
cursor.execute('select * from user where user=%s and password=%s' % (name,password))
    
```

## 2.读配置文件conf.yml
>详见代码：mysql_util.py


## 3. DBUtils 
> 以上的方法都不好，原因是没有使用数据库连接池

参考文章：  
- python DbUtils 使用教程  
https://blog.csdn.net/jacke121/article/details/79852146  

- python使用DBUtils连接部分主流数据库  
https://blog.csdn.net/danengbinggan33/article/details/80667204


### 3.1 安装DBUtils
```bash
pip install DBUtils
```
### 3.2 DB-API 2规范的相关数据库连接模块
```bash
pip install pymysql（mysql）
pip install pymssql（sqlserver）
pip install cx_Oracle（oracle）
pip install phoenixdb（hbase）
pip install sqlite3（sqlite3 python自带）
```
### 3.3 详见mysql_util.py


