## 爬虫入门和urllib

#### 一、爬虫介绍

##### 什么是爬虫Spider

```
爬虫：网络爬虫又称为网络蜘蛛Spider,网络蚂蚁,网络机器人等,可以自动化浏览网络中的信息,当浏览信息的时候需要按照我们的规定的规则进行,这些规则称之为网络爬虫算法,使用python可以很方便的写出爬虫程序,进行互联网信息的自动化检索

网 ： 互联网
蜘蛛网： 互联网理解为蜘蛛网
爬虫： 蜘蛛
```

##### Python爬虫的优势

```python
PHP: 虽然是世界上最好的语言,但是天生不是干爬虫的命,php对多线程,异步支持不足,并发不足,爬虫是工具性程序,对速度和效率要求较高。

Java: 生态圈完善,是Python最大的对手,但是java本身很笨重,代码量大,重构成本比较高,任何修改都会导致大量的代码的变动.最要命的是爬虫需要经常修改部分代码
# 爬虫 => 反爬  => 反反爬 => 反反反爬... 

C/C++: 运行效率和性能几乎最强,但是学习成本非常高,代码成型较慢,能用C/C++写爬虫,说明能力很强,但不是最正确的选择.

# SQL: 专门用于关系型数据库的
# Shell: 运维
# JavaScript： DOM,事件，Ajax
Python: 语法优美,代码简洁,开发效率高, 三方模块多,调用其他接口也方便, 有强大的爬虫Scrapy,以及成熟高效的scrapy-redis分布策略

```

##### 学习Python爬虫需要掌握什么

```
Python基础语法
HTML基础
CSS基础
JavaScript语言基础
```



#### 二、Python3中开发爬虫

##### 示例：模拟百度搜索

```python
import urllib.request

# 模拟百度搜索
def baiduAPI(wd):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }

    url = "https://www.baidu.com/s?wd=" + wd
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read().decode('utf-8')

if __name__ == "__main__":
    wd = input("请输入你要查找的内容:")

    response = baiduAPI(wd)
    print(response)
```



#### 抓取HTML数据

##### 示例： urllib.request爬取百度

```python
import urllib
from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

# 创建请求对象
req = urllib.request.Request("http://www.baidu.com", headers=headers)

response = urllib.request.urlopen(req)
print(response.info())  # 响应信息
print(response.read())  # 二进制
print(response.read().decode('utf-8'))  # 字符串
```



#### 抓取异步数据

##### 示例：抓取豆瓣电影

```python
import urllib
from urllib import request
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0"

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
content = response.read().decode()  # json数据

data = json.loads(content)
movie_list = data.get('data')

for movie in movie_list:
    title = movie.get('title')
    casts = movie.get('casts')
    print(title, casts)

```

#### 下载文件和图片

```python
# 参数1： 需要下载的url
# 参数2： 需要写入的文件路径
request.urlretrieve("http://www.baidu.com", r"baidu.html")
request.urlcleanup()  # 清除缓存

# 下载图片
request.urlretrieve("https://www.baidu.com/img/bd_logo1.png", r"baidu.png")
request.urlcleanup()  # 清除缓存
```




