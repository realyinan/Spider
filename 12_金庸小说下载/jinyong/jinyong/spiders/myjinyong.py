import scrapy
from jinyong.items import *


class MyjinyongSpider(scrapy.Spider):
    name = "myjinyong"
    allowed_domains = ["www.jinyongbook.com"]
    start_urls = ["https://www.jinyongbook.com"]

    def parse(self, response, **kwargs):
        pass
        print('*'*80)
        li_list = response.xpath('//ul[@class="shuming"]/li')
        for li in li_list:
            # 小说名
            xs_name = li.xpath('./p/a/text()').get()
            # 小说链接
            xs_link = 'https://www.jinyongbook.com/' + li.xpath('./p/a/@href').get()
            # print(xs_name, xs_link)

            yield scrapy.Request(
                url=xs_link,
                callback=self.parse_zhangjie,
                cb_kwargs={'xs_name': xs_name}
            )

    def parse_zhangjie(self, response, **kwargs):
        xs_name = kwargs['xs_name']

        zj_list = response.xpath('//div[@class="lb"]/ul/li')
        for zj in zj_list:
            zj_name = zj.xpath('./a/text()').get()
            zj_link = 'https://www.jinyongbook.com/xiudingban/feihuwaizhuan/' + zj.xpath('./a/@href').get()
            # print(zj_name, zj_link)

            yield scrapy.Request(
                url=zj_link,
                callback=self.parse_content,
                cb_kwargs={
                    'xs_name': xs_name,
                    'zj_name': zj_name
                }
            )
        pass

    def parse_content(self, response, **kwargs):
        xs_name = kwargs['xs_name']
        zj_name = kwargs['zj_name']

        zj_content = response.xpath('//div[@class="content"]/figure//td').get()
        # print(zj_content)

        # 把数据传到管道中
        yield JinyongItem(
            xs_name=xs_name,
            zj_name=zj_name,
            zj_content=zj_content
        )
        pass
