import scrapy
from dangdang.items import *


class MydandangSpider(scrapy.Spider):
    name = "mydandang"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html"]

    def parse(self, response, **kwargs):
        pass
        print('*'*80)
        
        # xpath
        li_list = response.xpath('//*[@id="component_59"]/li')
        for li in li_list:
            title = li.xpath('./a[1]/@title').get()
            price = li.xpath('./p[@class="price"]/span[1]/text()').get()
            # print(title, price)
            yield DangdangItem(title=title, price=price)

