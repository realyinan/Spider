from urllib import request
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'

req = request.Request(url=url, headers=headers)

response = request.urlopen(req)

res = response.read().decode()  # 字符串
# print(res)
print(type(res))

# json解析: 将字符串=>字典
d = json.loads(res)
# print(d)
print(type(d))

# 从字典中获取你想要的数据
data_list = d['data']
for data in data_list:
    title = data['title']
    directors = data['directors']
    print(title, directors)

    # 存储数据
    with open('01_爬虫入门和urllib\douban.csv', 'a', encoding='utf-8') as fp:
        fp.write(f'{title}, {directors}\n')