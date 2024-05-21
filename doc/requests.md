## Requests

```python
虽然Python的标准库中 urllib.request 模块已经包含了平常我们使用的大多数功能，但是它的 API 使用起来让人感觉不太好，而 Requests 自称 “HTTP for Humans”，说明使用更简洁方便。

requests 唯一的一个非转基因的 Python HTTP 库，人类可以安全享用：

requests 继承了urllib2的所有特性。Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。

requests 的底层实现其实就是 urllib3
requests 的文档非常完备，中文文档也相当不错
Requests 能完全满足当前网络的需求，支持Python 2.6以上。

开源地址：https://github.com/kennethreitz/requests
中文文档 API：http://docs.python-requests.org/zh_CN/latest/index.html
```

#### 安装方式
```python
pip安装:
pip install requests
```



### Requests使用

#### GET请求和POST请求

##### GET请求

```python
最基本的GET请求可以直接用get方法
response = requests.get("http://www.baidu.com/")

也可以这么写
# response = requests.request("get", "http://www.baidu.com/")

添加 headers 和 查询参数：
	如果想添加 headers，可以传入headers参数来增加请求头中的headers信息。如果要将参数放在url中传递，可以利用params参数。
```
##### POST请求
###### 示例：百度翻译

```python
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Cookie': ''  # 需要从浏览器url请求头中获取最新的Cookie
}
# POST请求
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
# POST参数
data = {
    "from": "en",
    "to": "zh",
    "query": "hello",
    "transtype": "translang",
    "simple_means_flag": 3,
    "sign": "54706.276099",
    "token": "c8b25a5b3debbe1ae3b9d0deef581968",
    "domain": "common"
}

response2 = requests.post(url, data=data, headers=headers)
result = response2.json()
# print(result)
print(result['trans_result']['data'][0]['dst'])

```


