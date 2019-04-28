# coding = utf-8

from selenium import webdriver

from selenium.webdriver.common.by import By


driver_path = r'D:\python\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("http://www.taobao.com")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_third = browser.find_element_by_xpath("//input[@id='q']")
input_four = browser.find_element(By.ID, 'q')


print(input_first)
print(input_second)
print(input_third)
print(input_four)

browser.close()
browser.quit()
