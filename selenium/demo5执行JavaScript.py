# coding = utf-8
from selenium import webdriver

driver_path = r'D:\python\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("http://www.zhihu.com/explore")
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
