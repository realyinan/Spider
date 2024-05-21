BOT_NAME = "jinyong"

SPIDER_MODULES = ["jinyong.spiders"]
NEWSPIDER_MODULE = "jinyong.spiders"

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {
   "jinyong.pipelines.JinyongPipeline": 300,
}

# FEED_EXPORT_ENCODING = "utf-8"
