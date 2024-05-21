import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

proxies = {
    "http": "112.17.16.238:80",
    # "https": "125.123.151.12:5443"

}

response = requests.get(url='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0', headers=headers, proxies=proxies)

res = response.json()

data_list = res['data']

for data in data_list:
    title = data['title']
    actors = data['casts']
    print(f"{title}: {actors}")

