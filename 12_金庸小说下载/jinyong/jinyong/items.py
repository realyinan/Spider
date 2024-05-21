import scrapy


class JinyongItem(scrapy.Item):
    xs_name = scrapy.Field()
    zj_name = scrapy.Field()
    zj_content = scrapy.Field()
    pass
