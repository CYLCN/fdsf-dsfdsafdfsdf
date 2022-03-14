# 1. 有对应的浏览器
# 2. 浏览器对应的驱动（注意版本的问题），还需要将浏览器驱动放置到环境变量
# 3. python需要安装selenium  【pip install selenium】

# import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 利用webdriver打开指定的浏览器
# Chrome 注意是大写的C
# 英文、数字、下划线组成的，且不能用数字开头
driver = webdriver.Chrome()


# 访问对应的url(网址)
driver.get('https://www.baidu.com')

# 做一系列的操作
# 1. 找到输入框并点击
# driver.find_element_by_id(id属性的值) 利用id属性的值，查找元素
# input_tag = driver.find_element_by_id('kw')
# find_element 接收两个参数，第一个参数是查找的方式，第二个参数是对应的值
# input_tag = driver.find_element(By.ID,'kw')
# input_tag = driver.find_element(By.CSS_SELECTOR,'#kw')

# 点击
# 元素是可以点的，但元素点了以后的结果，并不是元素
input_tag = driver.find_element(By.ID,'kw')
input_tag.click()
# 2. 向输入框中输入内容
input_tag.send_keys('python')
# 3. 找到【百度一下】按钮并点击
driver.find_element(By.ID,'su').click()

# 不同的对象拥有不同的方法

time.sleep(10)
# 退出浏览器
driver.quit()