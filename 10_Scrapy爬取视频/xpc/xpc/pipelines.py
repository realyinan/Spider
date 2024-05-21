from itemadapter import ItemAdapter
import pymysql


class XpcPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(
            user='root',
            password='2046',
            database='spider'
        )
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        # print(item)
        sql = f'''INSERT INTO xpc (pid, title, cover, category, duration, publish_time, content, play_counts, like_counts, video, video_format)
                VALUES ('{item['pid']}', '{item['title']}', '{item['cover']}', '{item['category']}', '{item['duration']}', '{item['publish_time']}', '{item['content']}', '{item['play_counts']}', '{item['like_counts']}', '{item['video']}', '{item['video_format']}')'''

        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        else:
            print('插入成功')
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
