BOT_NAME = "dangdang"

SPIDER_MODULES = ["dangdang.spiders"]
NEWSPIDER_MODULE = "dangdang.spiders"

USER_AGENT = "dangdang (+http://www.yourdomain.com)"

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3
 
ITEM_PIPELINES = {
   "dangdang.pipelines.DangdangPipeline": 300,
}

# FEED_EXPORT_ENCODING = "utf-8"
