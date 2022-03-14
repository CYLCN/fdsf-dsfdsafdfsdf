import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

span_tag = driver.find_element(By.CSS_SELECTOR,'.title-content-title')

# 获取标签文本
print(span_tag.text)

#
img_tag = driver.find_element(By.ID,'s_lg_img')
# 获取标签属性的值
src = img_tag.get_attribute('src')
print(src)

time.sleep(5)

# driver.quit()