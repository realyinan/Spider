import scrapy


class SinaItem(scrapy.Item):
    news_title = scrapy.Field()
    news_time = scrapy.Field()
    pass
