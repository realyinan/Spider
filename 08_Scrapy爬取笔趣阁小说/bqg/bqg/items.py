import scrapy


class BqgItem(scrapy.Item):
    xs_name = scrapy.Field()
    zj_name = scrapy.Field()
    zj_content = scrapy.Field()
    pass
