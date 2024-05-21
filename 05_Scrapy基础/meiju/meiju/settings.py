BOT_NAME = "meiju"
SPIDER_MODULES = ["meiju.spiders"]
NEWSPIDER_MODULE = "meiju.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "meiju (+http://www.yourdomain.com)"

# 是否遵守robots协议, 不遵守
ROBOTSTXT_OBEY = False

# 同时请求的最大并发数, 默认16
CONCURRENT_REQUESTS = 16

# 下载延迟 爬取的间隔
DOWNLOAD_DELAY = 3
 
# 配置管道  数字代表优先级, 越小, 优先级越高
ITEM_PIPELINES = {
   "meiju.pipelines.MeijuPipeline": 300,
}

# 指定编码方式为utf-8
FEED_EXPORT_ENCODING = 'utf-8'