import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# http常用的两种请求方式
# get方式
response = requests.get(url='https://www.youtube.com/', headers=headers)
# print(response)  # <Response [200]>
print(response.status_code)  # 获取状态码
# print(type(response))  # <class 'requests.models.Response'>
# print(response.text)  # 字符串内容: 已经自动解码二进制=>utf-8
# print(response.content)  # 二进制内容
# print(response.content.decode('utf-8'))
# print(response.json())

# 200 表式成功
#  1xx: 接收了一部分数据
#  2xx: 表式成功, 常见的是：200
#  3xx: 表式重定向, 常见的是: 301,302
#  4xx: 表式客户端出错了，常见的是：404,403,400
#  5xx: 表式服务端出错了，常见的是：500,502

