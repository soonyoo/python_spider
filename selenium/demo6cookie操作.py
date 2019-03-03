# coding = utf-8
from selenium import webdriver

driver_path = r'D:\python\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)
browser.get('https://www.baidu.com')

for cookie in browser.get_cookies():
    print(cookie)
