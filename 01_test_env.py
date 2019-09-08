import os


#coding=utf-8

# print('ok?')

# IMAGES_STORE = 'D:\\doubanimgs'
# BRAND_STORE = 'brand'
# IMG_NUM = '(30)'
# GIRLS_NAME = '保时捷5号车模'
# OK = 'OK'
#
# full_path = os.path.join(IMAGES_STORE,BRAND_STORE+IMG_NUM,GIRLS_NAME,OK)
# print(full_path)

a_list = ['a1','a2','a3','a4']
b_list = ['b1','b2','b3','b4']
for a1,b1 in zip(a_list,b_list):
    print(a1,b1)
