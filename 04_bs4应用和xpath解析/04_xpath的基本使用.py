from lxml import etree

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

# 创建xpath对象
mytree = etree.HTML(html_doc)
print(mytree)  # <Element html at 0x1c00abac040>
print('*'*100)

# 子节点: /
# 后代节点: //
print(mytree.xpath('/html'))
print(mytree.xpath('/html/head'))
print(mytree.xpath('//head'))
print(mytree.xpath('//a'))  # 默认找到所有的a标签
print('*'*100)

print(mytree.xpath('//a')[0])  # 第一个a标签
print(mytree.xpath('//a[1]'))  # 每个p标签下的第一个a标签
print(mytree.xpath('//p[2]/a[1]'))  # 第二个p标签下的第一个a标签
print('='*100)

# 属性
print(mytree.xpath('//a/@href'))
print(mytree.xpath('//p/@class'))
print('-'*100)

# 文本内容
print(mytree.xpath('//a/text()'))
print(mytree.xpath('//b/text()'))
print('+'*100)


# 谓词: 条件
# 按条件查找对应的标签
print(mytree.xpath('//p[2]/a[1]'))  # 第一个
print(mytree.xpath('//p[2]/a[last()]'))  # 最后一个
print(mytree.xpath('//p[2]/a[last()-1]'))  # 倒数第二个
print(mytree.xpath('//a[@id="link1"]'))  # 找到属性id是link1的a标签
print(mytree.xpath('//a[@class="boy"]'))
print('^'*100)

# 通配符
print(mytree.xpath('//*[@class="boy"]'))
print('-'*100)


# 较少使用
# 或 | 
print(mytree.xpath('//*[@class="boy"] | //b'))
print('+'*100)

# 包含: contains()
print(mytree.xpath('//a[contains(text(), "ci")]/text()'))
print(mytree.xpath('//a[contains(@href, "ci")]/text()'))


# 练习: 查找第二个p标签中的每个a标签的内容和href属性值
a_list = mytree.xpath('//p[2]/a')

for a in a_list:
    name = a.xpath('./text()')
    href = a.xpath('./@href')
    print(name, href)