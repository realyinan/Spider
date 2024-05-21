from itemadapter import ItemAdapter
import pymysql


class MeijuPipeline:
    # 存储item
    # 写多少个yield, 这里就会调用多少次
    def process_item(self, item, spider):

        print('item:', item)

        # 存储数据
        # 1. 存入csv文件
        # with open('mj.csv', 'a', encoding='utf-8') as fp:
        #     fp.write(f'{item["meiju_name"]}, {item["meiju_type"]}\n')
             
        #     fp.write(f'{item["name"]}, {item["type"]}\n')

        # 2. 存入Mysql
        with self.db.cursor() as cur:
            sql = f'insert into meiju(name, type) value("{item["name"]}", "{item["type"]}")'
            cur.execute(sql)
        
        self.db.commit()
        print('插入成功')
        return item
    
    # 开始爬取的时候自动调用
    def open_spider(self, spider):
        print('开始爬取..')
        self.db = pymysql.connect(user='root', password='2046', database='spider')

    # 结束爬取的时候自动调用
    def close_spider(self, spider):
        print('爬取结束')
        self.db.close()





