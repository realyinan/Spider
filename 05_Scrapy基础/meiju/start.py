import scrapy.cmdline

# scrapy.cmdline.execute('scrapy crawl mymeiju --nolog'.split())

# -o 快速存储
scrapy.cmdline.execute('scrapy crawl mymeiju --nolog -o meiju.csv'.split())

# 创建项目
# scrapy startproject meiju

# 创建爬虫文件
# scrapy genspider mymeiju

# 运行项目
# scrapy crawl mymeiju
# scrapy crawl mymeiju --nolog  # 没有log
# scrapy crawl mymeiju -o meiju.csv
# scrapy crawl mymeiju -o meiju.csv
# scrapy crawl mymeiju -o meiju.xml



