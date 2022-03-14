from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器
driver = webdriver.Chrome()

# 访问网页
driver.get('https://sz.esf.fang.com/')

# 查找节点
# 一边调试一边写
# b_tag = driver.find_element(By.CSS_SELECTOR,'span.red')
# price = b_tag.text
# print(price)

# dd标签下的第三个span标签
# find_element  默认返回的是第一个满足条件的元素
span_tag = driver.find_element(By.CSS_SELECTOR,'dd>span:nth-child(3)')
# print(span_tag.text)
# print(span_tag)
# print('=========================')
# 我们需要所有满足条件的
# find_elements  返回所有满足条件的元素
# 返回的是一个容器(列表)，容器里面装着所有的元素
tag_list = driver.find_elements(By.CSS_SELECTOR,'dd>span:nth-child(3)')
# print(tag_list)
# 从列表中取出第二个
# print(tag_list[1].text)

# 从列表中取出所有的所有
for i in tag_list:
    print(i.text)
    print('=========')


driver.quit()
