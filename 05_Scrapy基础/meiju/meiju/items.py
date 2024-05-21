import scrapy


class MeijuItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    pass
