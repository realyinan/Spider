# yield在scrapy中的作用


# 爬虫文件
class MydangdangSpider():
    # 生成器函数
    def parse(self, response):
        for star in response:
            name = star["name"]
            movie = star["movie"]

            yield {'name': name, 'movie': movie}


# 管道文件
class DangdangPipeline():
    def process_item(self, item):
        print(item)
        return item


if __name__ == '__main__':
    # 响应数据
    response = [{"name": "鹿晗", "movie": "上海堡垒"},
                {"name": "吴亦凡", "movie": "老炮儿"}]
    
    # 创建管道对象
    pipline = DangdangPipeline()

    # 创建爬虫对象
    spider = MydangdangSpider()
    g = spider.parse(response)

    for item in g:
        # print(item)
        pipline.process_item(item)