BOT_NAME = "xpc"

SPIDER_MODULES = ["xpc.spiders"]
NEWSPIDER_MODULE = "xpc.spiders"

USER_AGENT = "xpc (+http://www.yourdomain.com)"

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {
   "xpc.pipelines.XpcPipeline": 300,
}

# FEED_EXPORT_ENCODING = "utf-8"
