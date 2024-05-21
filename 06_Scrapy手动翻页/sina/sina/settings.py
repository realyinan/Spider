BOT_NAME = "sina"

SPIDER_MODULES = ["sina.spiders"]
NEWSPIDER_MODULE = "sina.spiders"

USER_AGENT = "sina (+http://www.yourdomain.com)"

ROBOTSTXT_OBEY = False

# 并发数量
CONCURRENT_REQUESTS = 16
 
DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {
   "sina.pipelines.SinaPipeline": 300,
}

# FEED_EXPORT_ENCODING = "utf-8"
