from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

# 创建驱动
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 获取输入框标签
shuru = driver.find_element(by=By.ID, value='kw')
time.sleep(3)

# 输入框自动填充内容
shuru.send_keys('王家卫', Keys.ENTER)

 

input("please enter to continue........")