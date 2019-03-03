# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = r'D:\python\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)
# 请求百度url
browser.get("https://www.baidu.com")
# 1.第一步查找元素
input_tag = browser.find_element_by_id('kw')
# 2.第二步填入Python
input_tag.send_keys('Python')
# 3.暂停1秒
time.sleep(1)
# 4.清除输入的字符
input_tag.clear()
# 5.输入c++
input_tag.send_keys('c++')
# 6.按ENTER键
# input_tag.send_keys(Keys.ENTER)

# 6.点击[百度一下]
search_btn = browser.find_element_by_id('su')
search_btn.click()

