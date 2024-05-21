from itemadapter import ItemAdapter


class DangdangPipeline:
    def process_item(self, item, spider):
        # 存入csv
        with open('dangdang.csv', 'a', encoding='utf-8') as fp:
            fp.write(f'{item["title"]}, {item["price"]}\n')
        return item
