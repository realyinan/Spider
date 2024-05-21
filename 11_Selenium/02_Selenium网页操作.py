from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys

# 创建驱动
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 获取点击按钮
btn = driver.find_element(by=By.ID, value='su')  # 获取一个
# btn = driver.find_elements(by=By.CLASS_NAME, value='su')  # 获取多个

# 获取输入框标签
shuru = driver.find_element(by=By.ID, value='kw')
time.sleep(3)

# 输入框自动填充内容
shuru.send_keys('王家卫')
time.sleep(3)

# 点击按钮
btn.click()




input("please enter to continue........")