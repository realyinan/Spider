from itemadapter import ItemAdapter
import pymysql

class SinaPipeline:
    def process_item(self, item, spider):
        print('item: ', item)
        # 插入数据库中
        with open('sina.csv', 'a', encoding='utf-8') as fp:
            fp.write(f'{item["news_title"]}, {item["news_time"]}\n')
        return item
    
    

