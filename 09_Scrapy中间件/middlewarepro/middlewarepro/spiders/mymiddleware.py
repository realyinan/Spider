import scrapy


class MymiddlewareSpider(scrapy.Spider):
    name = "mymiddleware"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html"]

    def parse(self, response, **kwargs):
        pass
        print('*'*80)
        print(len(response.text))
