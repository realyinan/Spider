BOT_NAME = "bqg"

SPIDER_MODULES = ["bqg.spiders"]
NEWSPIDER_MODULE = "bqg.spiders"

USER_AGENT = "bqg (+http://www.yourdomain.com)"

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {
   "bqg.pipelines.BqgPipeline": 300,
}

 
# FEED_EXPORT_ENCODING = "utf-8"
