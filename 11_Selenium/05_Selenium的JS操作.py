from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://www.jd.com/')
time.sleep(5)


for i in range(10):
    driver.execute_script('window.scrollBy(0, 2000)')
    time.sleep(2)

# 移动之后查看数据源码
print(driver.page_source)


input()