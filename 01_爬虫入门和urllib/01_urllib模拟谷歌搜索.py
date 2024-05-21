from urllib import request

headers = {
    # 用户身份: 用户所在的浏览器版本和操作系统版本
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
# 百度搜索网址
url = 'https://www.google.com/search?q=%E7%BA%B1%E7%BB%AB'

# 创建Request请求对象
req = request.Request(url=url, headers=headers)

# 打开网页, 爬取数据
response = request.urlopen(req)  # <http.client.HTTPResponse object at 0x000001ADE00E51E0>

# read(): 得到相应数据内容
# info(): 响应信息
# decode(): 解码: 二进制=>字符串
# encode(): 编码: 字符串=>二进制
print(response.info())
result = response.read().decode()  # 二进制数据 b"Hello"

# 存储数据
with open(r'01_爬虫入门和urllib\result.html', 'w', encoding='utf-8') as fp:
    fp.write(result)