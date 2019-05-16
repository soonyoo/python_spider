# coding: utf-8

"""
时间格式处理
"""

import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)


# time.strftime(format[, t])

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

ymd = time.strftime("%Y-%m-%d", time.localtime())
ymd2 = time.strftime("%Y%m%d", time.localtime())
print(ymd[0:4])

print(ymd[5:7])

print(ymd[8:10])

print(ymd2)
print(ymd2[2:4])
print(ymd2[4:9])

# print()

