BOT_NAME = "middlewarepro"

SPIDER_MODULES = ["middlewarepro.spiders"]
NEWSPIDER_MODULE = "middlewarepro.spiders"

USER_AGENT = "middlewarepro (+http://www.yourdomain.com)"

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3

# 爬虫中间件
SPIDER_MIDDLEWARES = {
   "middlewarepro.middlewares.MiddlewareproSpiderMiddleware": 543,
}

# 下载器中间件
DOWNLOADER_MIDDLEWARES = {
   # 数字越小越优先
   # "middlewarepro.middlewares.MiddlewareproDownloaderMiddleware": 543,
   'middlewarepro.middlewares.UserAgentDownloaderMiddleware': 500,
   'middlewarepro.middlewares.ProxyDownloadMiddleware': 400
}

ITEM_PIPELINES = {
   "middlewarepro.pipelines.MiddlewareproPipeline": 300,
}

PROXIES = [
    "http://182.47.223.131:5063",
    "http://120.34.36.98:5064",
    "http://113.231.9.145:5062",
    "http://182.107.183.75:5064",
]
# FEED_EXPORT_ENCODING = "utf-8"
