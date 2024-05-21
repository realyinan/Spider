from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

# 无界面
options = ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com/')
print(driver.page_source)

