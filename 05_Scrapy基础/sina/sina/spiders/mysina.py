import scrapy
from sina.items import *


class MysinaSpider(scrapy.Spider):
    name = "mysina"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["https://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml"]

    def parse(self, response, **kwargs):
        pass
        print('*'*80)
        # x_path
        li_list = response.xpath('//*[@class="list_009"]/li')
        for li in li_list:
            news_title = li.xpath('./a/text()').get()
            news_time = li.xpath('./span/text()').get()

            yield SinaItem(news_title=news_title, news_time=news_time)