from itemadapter import ItemAdapter
import os


class JinyongPipeline:
    def process_item(self, item, spider):
        # print(item)
        xs_name = item['xs_name']
        zj_name = item['zj_name']
        zj_content = item['zj_content']


        # 存储路径
        path = r'C:\Users\19981\Desktop\Spider\12_金庸小说下载\xiaoshuo'

        # 每一部小说存储路径
        xs_path = os.path.join(path, xs_name)

        # 每一章的路径
        zj_path = os.path.join(xs_path, f'{zj_name}.txt')

        # 创建小说文件夹
        if not os.path.exists(xs_path):
            os.mkdir(xs_path)

        # 开始存储
        with open(zj_path, 'w', encoding='utf-8') as fp:
            fp.write(zj_content)
            fp.flush()

        return item
