# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By


driver_path = r'D:\python\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.taobao.com")
# 方法1
# lis = browser.find_elements_by_css_selector('.service-bd li')
# for li in lis:
#     print(li)

# 方法2
lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
for li in lis:
    print(li)


browser.close()
