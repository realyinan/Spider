import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'http://quote.stockstar.com/fund/stock.html'

response = requests.get(url=url, headers=headers)
# res = response.text  # 默认utf-8转码
res = response.content.decode('gbk')

# 第一种方式
soup = BeautifulSoup(markup=res, features='lxml')
# ul = soup.find_all('ul', id="index_data_0")[0]
# li_list = ul.find_all('li')
# for li in li_list:
#     code = li.find_all('a')[0].text
#     name = li.find_all('a')[1].text
#     print(code, name)

# 第二种方式
li_list = soup.select('#index_data_0 li')
for li in li_list:
    code = li.select('a')[0].text
    name = li.select('a')[1].text
    print(code, name)
    # time.sleep(0.1)

