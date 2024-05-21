from urllib import request

# 下载图片
request.urlretrieve(
    url='https://i.pinimg.com/564x/b4/58/3f/b4583f484f26da71bdaf85730b498a7c.jpg', 
    filename=r'01_爬虫入门和urllib\high_heels.jpg')
# 清除缓存
request.urlcleanup()

