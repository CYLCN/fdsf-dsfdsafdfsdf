import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

# 点击登录按钮
driver.find_element(By.ID,'s-top-loginbtn').click()

time.sleep(3)
# 找到用户名输入框，并输入用户名
driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__userName').send_keys('1111111111')

# 找到密码输入框，并输入密码
driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__password').send_keys('123456')

# 找到登录按钮，并点击
# 当采用css选择器，且class简写为点时，如果class的值有多个(中间有空格的)，需要将空格替换成.
# 如果class不简写成点，那就原封不动
# driver.find_element(By.CSS_SELECTOR,'.pass-button.pass-button-submit').click()
# driver.find_element(By.CSS_SELECTOR,'[class="pass-button pass-button-submit"]').click()
driver.find_element(By.ID,'TANGRAM__PSP_11__submit').click()

time.sleep(5)

# driver.quit()