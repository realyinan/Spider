from itemadapter import ItemAdapter
import pymysql

class SinaPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(user='root', password='2046', database='spider')
        self.cur = self.db.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()

    def process_item(self, item, spider):
        print('item: ', item)
        # 插入数据库中
        sql = f'insert into sina(news_title, news_time)' \
              f'value("{item["news_title"]}", "{item["news_time"]}")'
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print('插入失败')
            self.db.rollback()
        else:
            print('插入成功')

        return item
    
    

