from bs4 import BeautifulSoup
import lxml

html_doc = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title">
            <b>The Dormouse's story</b>
        </p>
        <p class="story">
            <a class="sister" href="http://elsie" id="link1">Elsie</a>
            <a class="sister" href="http://lacie" id="link2">Lacie</a>
            <a class="sister" href="http://tillie" id="link2">Tillie</a>
        </p>
        <p class="story">
            <a class="boy" href="http://libai" id="link1">...</a>
        </p>
    </body>
</html>
'''

soup = BeautifulSoup(markup=html_doc, features='lxml')
# print(soup, type(soup))  #  <class 'bs4.BeautifulSoup'>

# 默认情况下只能获取到第一个标签
print(soup.head)
print(soup.b)
print(soup.a)
print('*'*50)

# 得到标签的属性
print(soup.a['class'])
print(soup.a['href'])
print(soup.a['id'])
print('*'*50)

# 获取标签的内容
print(soup.p.text)
print(soup.a.text)
print('*'*50)

# 找到所有匹配的标签, 返回列表
print(soup.find_all('a'))
print(soup.find_all('a', id='link1'))
print(soup.find_all(['b', 'title']))
print('*'*50)


# css 选择器
print(soup.select('.boy'))
print(soup.select('#link1'))
print('*'*50)


sister_list = soup.select('.sister')
for sister in sister_list:
    print(sister.text)
    print(sister['href'])
print('*'*50)


# 层级选择器
print(soup.select('p .boy'))























