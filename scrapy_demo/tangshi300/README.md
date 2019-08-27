# 唐诗300首scrapy实现

> 知识点：
1. scrapy 中使用 xpath
2. scrapy.Request中的meta参数的使用
3. 把数据存到csv中的实现
```python
 方法一：可以直接通过加命令参数生成csv
cmdline.execute("scrapy crawl tangshi -o tangshi300.csv -t csv".split())
 方法二：在Pipeline中实现（这种方法灵活一些）
参见：pipelines.py
```
