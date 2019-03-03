# coding = utf-8
#
# from selenium import webdriver
#
# #
# driver = webdriver.chrome(executable_path = driver_path)
# driver.get('https://www.baidu.com')
# print(driver.page_resource)

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chromedriver绝对路径
driver_path = r'D:\python\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)
# browser = webdriver.Chrome()


browser.get("http://www.baidu.com")
input_tag = browser.find_element_by_id('kw')
input_tag.send_keys('Python')
# 按ENTER键
# input_tag.send_keys(Keys.ENTER)
# 点击搜索键
submit_tag = browser.find_element_by_id('su')
submit_tag.click()
# print(browser.page_source)
# browser.close()


# class SeleniumOpt(object):
#     def __init__(self):
#
#         pass
