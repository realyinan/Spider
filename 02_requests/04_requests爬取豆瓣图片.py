import requests
from urllib import request
from threading import Thread

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'

response = requests.get(url=url, headers=headers)

res = response.json()

data_list = res['data']

threads = []

def image_download(url, filename):
    request.urlretrieve(url=url, filename=filename)
    request.urlcleanup



for data in data_list:
    threads.append(Thread(target=image_download, 
                          args=(data['cover'], f"02_requests\images\{data['title']}.jpg")))

for t in threads:
    t.start()




 

