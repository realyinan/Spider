import scrapy
import os
from bqg.items import *

class MybqgSpider(scrapy.Spider):
    name = "mybqg"
    allowed_domains = ["wxdzs.net"]
    start_urls = ["https://www.wxdzs.net/wxlist/%E7%8E%84%E5%B9%BB.html"]

    # 小说列表
    def parse(self, response, **kwargs):
        pass
        print('*'*80)
        # xpath
        a_list = response.xpath('//div[@style="margin: 10px; overflow: hidden; border-bottom: 1px dotted #d6d6d6; padding-bottom: 20px;  position: relative;"]/div[@class="right_wid"]/div[@class="margin0h5"]/a[1]')
        for a in a_list[:4]:
            # 小说名字
            xs_name = a.xpath('./text()').get()
            # 小说href
            xs_href = "https://www.wxdzs.net/wxchapter/" + os.path.basename(a.xpath('./@href').get())
            # print(xs_name, xs_href)

            # 发送请求: 爬取章节页面
            yield scrapy.Request(
                url=xs_href,
                callback=self.parse_detail,
                # 传参数, 数据
                cb_kwargs={
                    'xs_name': xs_name
                }
            )

    # 每一部小说的章节
    def parse_detail(self, response, **kwargs):
        # 得到传入的参数
        xs_name = kwargs['xs_name']
        pass
        # 解析章节数据
        span_list = response.xpath('//div[@style=" height:40px; line-height:40px; border-bottom: 1px dotted #ccc; overflow:hidden; font-size:14px;"]/span')
        for span in span_list[:4]:
            zj_name = span.xpath('./a/text()').get()
            zj_link = "https://www.wxdzs.net" + span.xpath('./a/@href').get()
            # print(zj_name, zj_link)

            yield scrapy.Request(
                url=zj_link,
                callback=self.parse_content,
                cb_kwargs={
                    'xs_name': xs_name,
                    'zj_name': zj_name
                }
            )


    # 每一章小说内容
    def parse_content(self, response, **kwargs):
        xs_name = kwargs['xs_name']
        zj_name = kwargs['zj_name']
        pass
        # get() : 取结果列表中的第一个值
        # getall(): 取结果列表中的所有值
        content_list = response.xpath('//div[@id="Lab_Contents"]/p/text()').getall()
        zj_content = '\n'.join(content_list)
        # print(zj_content)

        # 将数据传入管道
        yield BqgItem(xs_name=xs_name, zj_name=zj_name, zj_content=zj_content)




