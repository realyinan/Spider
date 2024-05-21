import scrapy


class XpcItem(scrapy.Item):
    # 作品表主键
    pid = scrapy.Field()
    # 作品标题
    title = scrapy.Field()
    # 视频缩略图
    cover = scrapy.Field()
    # 视频分类
    category = scrapy.Field()
    # 播放时长
    duration = scrapy.Field()
    # 发表事件
    publish_time = scrapy.Field()
    # 作品描述
    content = scrapy.Field()
    # 播放次数
    play_counts = scrapy.Field()
    # 点赞次数
    like_counts = scrapy.Field()
    # 视频链接
    video = scrapy.Field()
    # 视频格式
    video_format = scrapy.Field()
    pass
