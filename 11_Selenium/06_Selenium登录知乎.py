from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.zhihu.com/signin?next=%2F'

# 创建驱动
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

# 获取QQ登录按钮
QQ = driver.find_element(
    by=By.XPATH, 
    value='//span[@class="Login-socialButtonGroup"]/button[2]'
    )
# 点击
QQ.click()

# 等待15s(手动登录)
time.sleep(20)

print(driver.page_source)

input()

