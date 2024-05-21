import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = requests.get(url='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0', headers=headers)

print(response.status_code)
# print(response.content)
# print(response.text)
res = response.json()

data_list = res['data']

for data in data_list:
    title = data['title']
    rate = data['rate']

    with open('02_requests\douban.csv', 'a', encoding='utf-8') as fp:
        fp.write(f'{title}, {rate}\n')
