import scrapy
from sina.items import *
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# 自动翻页: CrawlSpider

class MysinaSpider(CrawlSpider):
    name = "mysina"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["https://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml"]

    # 写Rules属性
    rules = [
        # Rule对象: 规则
        Rule(
            # 链接规则
            link_extractor=LinkExtractor(
                # 对超链接href的网址做匹配, 写正则表达式
                allow=(r'index_\d+\.shtml'),
                # 限制查找a标签的范围
                restrict_xpaths=('//div[@class="pagebox"][1]'),
            ),
            # 回调函数
            callback='parse_item',
            # 是否跟随
            # 如果为True, 则会继续爬取子网页中的数据
            follow=True

        )

    ]


    def parse_item(self, response, **kwargs):
        # x_path
        li_list = response.xpath('//*[@class="list_009"]/li')
        for li in li_list:
            news_title = li.xpath('./a/text()').get()
            news_time = li.xpath('./span/text()').get()

            yield SinaItem(news_title=news_title, news_time=news_time)
        