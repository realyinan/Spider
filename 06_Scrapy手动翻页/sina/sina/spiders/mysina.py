import scrapy
from sina.items import *


class MysinaSpider(scrapy.Spider):
    name = "mysina"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["https://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml"]

    # 手动翻页
    # 页码
    page = 1

    def parse(self, response, **kwargs):
        # x_path
        li_list = response.xpath('//*[@class="list_009"]/li')
        for li in li_list:
            news_title = li.xpath('./a/text()').get()
            news_time = li.xpath('./span/text()').get()

            yield SinaItem(news_title=news_title, news_time=news_time)
        print(f'第{self.page}页爬取结束')

        if self.page < 5:
            self.page += 1

            url = f"https://roll.news.sina.com.cn/news/gnxw/gdxw1/index_{self.page}.shtml"

            # 发送请求
            # scrapy.Request() : get请求
            # scrapy.FormRequest() : post请求
            # callback: 指定那个函数来接收相应数据
            yield scrapy.Request(url, callback=self.parse)

            # yield:
            # 1. 返回item
            # 2. 返回Request