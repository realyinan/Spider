from selenium import webdriver
import time



# 使用Chrome
driver = webdriver.Chrome()
# print(driver)

# 打开网页
driver.get('https://www.baidu.com/')
time.sleep(5)

# 网页源码

# print(driver.page_source)


# 关闭
# driver.close()  # 关闭一个窗口
driver.quit()  # 退出浏览器


input("Please enter to continue")

