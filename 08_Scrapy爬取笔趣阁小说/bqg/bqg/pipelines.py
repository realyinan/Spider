from itemadapter import ItemAdapter
import os



class BqgPipeline:
    def process_item(self, item, spider):
        # print(item)
        xs_name = item['xs_name']
        zj_name = item['zj_name']
        zj_content = item['zj_content']

        # 存储文件夹
        path = r'C:\Users\19981\Desktop\spider\08_Scrapy爬取笔趣阁小说\xiaoshuo'

        # 小说文件路径
        xs_path = os.path.join(path, xs_name)

        # 创建小说文件夹
        if not os.path.exists(xs_path):
            os.mkdir(xs_path)
        
        # 章节路径
        zj_path = os.path.join(xs_path, f'{zj_name}.txt')
        print(zj_path)

        # 存储小说
        with open(zj_path, 'w', encoding='utf-8') as fp:
            fp.write(zj_content)
            fp.flush()

        print(f'{xs_name} -> {zj_name} OK')


        return item
