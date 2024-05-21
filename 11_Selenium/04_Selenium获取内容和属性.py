from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 获取百度热搜内容
span_list = driver.find_elements(by=By.CSS_SELECTOR, value='.title-content-title')
for span in span_list:
    print(span.get_attribute('innerText'))
    print(span.get_attribute('class'))
    print('-'*80)

input('enter')