import scrapy
from meiju.items import *

class MymeijuSpider(scrapy.Spider):
    name = "mymeiju"  # 爬虫名: 唯一
    allowed_domains = ["www.meijutt.net"]  # 允许的域名
    start_urls = ["https://www.meijutt.net/new100.html"]  # 开始爬取的url列表

    # parse:
    # 1. 自动接受响应数据
    # 2. parse函数会被自动调用
    def parse(self, response, **kwargs):
        # print(response)
        # print(response.text)  # 文本内容
        # print(response.body)  # 二进制内容
        # print(response.json())  # json解析

        # xpath解析
        # response已经集成了xpath
        li_list = response.xpath('//*[@class="top-list  fn-clear"]/li')
        for li in li_list:
            # 美剧名字
            meiju_name = li.xpath('./h5//a/text()').get()
            # 美剧类型
            meiju_type = li.xpath('./*[@class="mjjq"]/text()').get()

            # print(meiju_name, meiju_type)

            # 数据传入piplines中
            # yield返回数据(item 或 字典)
            # yield {'meiju_name': meiju_name, 'meiju_type': meiju_type}

            # yield MeijuItem(name=meiju_name, type=meiju_type)

            item = MeijuItem()
            item['name'] = meiju_name
            item['type'] = meiju_type
            yield item


