import requests
from bs4 import BeautifulSoup
import pymysql

# 第一步: 连接数据库
db = pymysql.connect(user='root',passwd='2046',
                     host='localhost',port=3306,
                     database='spider')

# 第二步; 创建游标
cursor = db.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'http://quote.stockstar.com/fund/stock.html'

response = requests.get(url=url, headers=headers)

res = response.content.decode('gbk')

soup = BeautifulSoup(markup=res, features='lxml')
 
li_list = soup.select('#index_data_0 li')
for li in li_list:
    code = li.select('a')[0].text
    name = li.select('a')[1].text
    print(code, name)

    # 第三步: 插入数据
    sql = f'insert into stock(code, name) values("{code}", "{name}")'
    cursor.execute(sql)

# 第四步: 提交
db.commit()

# 第五步: 关闭连接
cursor.close()
db.close()
