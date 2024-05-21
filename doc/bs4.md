## bs4

#### Beautiful Soup 4 文档 

https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

##### 示例：爬取股票基金

```python
import urllib
from urllib import request
from bs4 import BeautifulSoup

stockList = []

def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib.request.Request(url, headers=headers)  # 请求，修改，模拟http.
    data = urllib.request.urlopen(request).read()  # 打开请求，抓取数据
    
    soup = BeautifulSoup(data, "lxml", from_encoding="gb2312")
    mytable = soup.select("#datalist")
    for line in mytable[0].find_all("tr"):
        print(line.get_text())  # 提取每一个行业
        print(line.select("td:nth-of-type(3)")[0].text) # 提取具体的某一个

if __name__ == '__main__':
    download("http://quote.stockstar.com/fund/stock.html")

```
### 存入数据库

```python
import pymysql

# 存入数据库
def save_job(tencent_job_list):

    # 连接数据库
    db = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root",database='tencent1', charset='utf8')
    # 游标
    cursor = db.cursor()
	
    # 遍历，插入job
    for job in tencent_job_list:
        sql = 'insert into job(name, address, type, num) VALUES("%s","%s","%s","%s") ' % (job["name"], job["address"], job["type"], job["num"])
        cursor.execute(sql)
        db.commit()

    cursor.close()
    db.close()
```



