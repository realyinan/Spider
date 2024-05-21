import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'http://quote.stockstar.com/fund/stock.html'

response = requests.get(url, headers=headers)
res = response.content.decode('gbk')

# xpath解析
mytree = etree.HTML(res)

li_list = mytree.xpath('//ul[@id="index_data_0"]/li')

for li in li_list:
    code = li.xpath('./span/a/text()')[0]
    name = li.xpath('./a/text()')[0]
    print(code, name)

    with open(r'04_bs4应用和xpath解析\stock.csv', 'a', encoding='utf-8') as fp:
        fp.write(f"{code}, {name}\n")