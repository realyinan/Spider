from urllib import request
import requests
from bs4 import BeautifulSoup
from threading import Thread
import uuid
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'https://telegra.ph/%E9%AB%98%E6%A9%8B%E3%81%97%E3%82%87%E3%81%86%E5%AD%90-%E3%81%9F%E3%81%8B%E3%81%97%E3%82%87%E3%83%BCLast-show-%E9%80%B1%E5%88%8A%E3%83%9D%E3%82%B9%E3%83%88%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E5%86%99%E7%9C%9F%E9%9B%86-85P-05-26'

response = requests.get(url=url, headers=headers)
res = response.text

threads = []

def image_download(url, filename):
    request.urlretrieve(url=url, filename=filename)
    request.urlcleanup

soup = BeautifulSoup(markup=res, features='lxml')
img_tags = soup.select('figure img')

for img in img_tags:
    threads.append(Thread(target=image_download, args=('https://telegra.ph'+img['src'], f"03_代理ip和bs4使用\images\{os.path.basename(img['src'])}")))
    print(os.path.basename(img['src']), '-下载完成')

for t in threads:
    t.start()

for t in threads:
    t.join()

print('所有图片下载完成')
 