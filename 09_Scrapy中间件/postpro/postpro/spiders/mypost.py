import scrapy


class MypostSpider(scrapy.Spider):
    name = "mypost"
    allowed_domains = ["baidu.com"]
    # start_urls = ["https://baidu.com"]

    # 1.需要使用post请求
    # 2.第一个请求就是post请求
    # 需要重写start_requests
    def start_requests(self):

        yield scrapy.FormRequest(
            url='https://fanyi.baidu.com/sug',
            callback=self.parse,
            formdata={'kw': 'request'}  # post请求的参数
        )


    def parse(self, response, **kwargs):

        pass
        res = response.json()
        print(res)

        
