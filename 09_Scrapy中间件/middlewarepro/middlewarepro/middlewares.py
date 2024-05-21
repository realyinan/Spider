from scrapy import signals

from itemadapter import is_item, ItemAdapter


class MiddlewareproSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # 3. response响应数据进入爬虫
    def process_spider_input(self, response, spider):
        print('3. response响应数据进入爬虫, process_spider_input')
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    # 4. 将结果传入管道
    def process_spider_output(self, response, result, spider):
        print('4. 将结果传入管道, process_spider_output')
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass
    
    # 1. 开始请求
    def process_start_requests(self, start_requests, spider):
        print('1. 开始请求, process_start_requests')
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class MiddlewareproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # 2. 处理请求, 在下载之前
    # 设置代理IP, User-Agent
    def process_request(self, request, spider):
        print('2. 处理请求, 在下载之前, process_request')
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 3. 处理响应, 在下载之后
    def process_response(self, request, response, spider):
        print('3. 处理响应, 在下载之后, process_response')
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    # 处理异常
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


import faker
# 自定义中间件
class UserAgentDownloaderMiddleware():
    # 下载之前
    def process_request(self, request, spider):
        # 通过faker得到随机的user-agent
        ua = faker.Faker().user_agent()
        print(ua)
        # 在请求头heades中设置User-Agent
        request.headers['User-Agent'] = ua
        return None
    
from middlewarepro.settings import PROXIES
import random
class ProxyDownloadMiddleware():
    # 下载之前
    def process_request(self, request, spider):
        # 设置随机代理IP
        proxy = random.choice(PROXIES)
        print(proxy)
        request.meta['proxies'] = proxy
        return None