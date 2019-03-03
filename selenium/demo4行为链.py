# coding = utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains

driver_path = r'D:\python\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)

# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

browser.get('https://www.baidu.com')
inputTag = browser.find_element_by_id('kw')
submitTag = browser.find_element_by_id('su')
# 1.加载行为链
actions = ActionChains(browser)
# 2.移动到输入框
actions.move_to_element(inputTag)
# 3.输入python
actions.send_keys_to_element(inputTag, 'python')
# 4.移动到[百度一下]按钮
actions.move_to_element(submitTag)
# 5.点击[百度一下]按钮
actions.click(submitTag)
# 6.执行
actions.perform()
