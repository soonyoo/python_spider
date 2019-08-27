from scrapy import cmdline

# 可以直接通过加命令参数生成csv
# cmdline.execute("scrapy crawl tangshi -o tangshi300.csv -t csv".split())

cmdline.execute("scrapy crawl tangshi".split())
