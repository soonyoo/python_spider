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
