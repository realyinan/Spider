BOT_NAME = "postpro"

SPIDER_MODULES = ["postpro.spiders"]
NEWSPIDER_MODULE = "postpro.spiders"

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

SPIDER_MIDDLEWARES = {
   "postpro.middlewares.PostproSpiderMiddleware": 543,
}

DOWNLOADER_MIDDLEWARES = {
   "postpro.middlewares.PostproDownloaderMiddleware": 543,
}


ITEM_PIPELINES = {
   "postpro.pipelines.PostproPipeline": 300,
}
 
FEED_EXPORT_ENCODING = "utf-8"
