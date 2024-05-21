import scrapy
import datetime
from xpc.items import *


class MyxpcSpider(scrapy.Spider):
    name = "myxpc"
    allowed_domains = ["xinpianchang.com"]
    start_urls = ["https://www.xinpianchang.com/api/xpc/v2/search?type=channel&page=1&per_page=20"]

    def parse(self, response, **kwargs):
        pass
        print('*'*80)
        result = response.json()
        # print(result)
        data_list = result['data']['list']
        for data in data_list:
            # 作品表主键
            pid = data['id']
            # 作品标题
            title = data['title']
            # 视频缩略图
            cover = data['cover']
            # 视频分类
            categories = data['categories']
            category = '|'.join([f'{cate["category_name"]}-{cate["sub"]["category_name"]}' for cate in categories])
            # 播放时长
            duration = data['duration']
            # 发表事件
            publish_time = datetime.datetime.fromtimestamp(data['publish_time']).strftime("%Y-%m-%d %H:%M:%S")
            # 作品描述
            content = data['content']
            # 播放次数
            play_counts = data['count']['count_view']
            # 点赞次数
            like_counts = data['count']['count_like']

            xpc_item = XpcItem(
                pid=pid,
                title=title,
                cover=cover,
                category=category,
                duration=duration,
                publish_time=publish_time,
                content=content,
                play_counts=play_counts,
                like_counts=like_counts
            )


            # 视频数据
            vid = data['video_library_id']
            video_url = f'https://mod-api.xinpianchang.com/mod/api/v2/media/{vid}?appKey=61a2f329348b3bf77&extend=userInfo%2CuserStatus'

            yield scrapy.Request(
                url=video_url,
                callback=self.parse_video,
                cb_kwargs={'xpc_item': xpc_item}
            )
        
    def parse_video(self, response, **kwargs):
        xpc_item = kwargs['xpc_item']

        # json解析
        result = response.json()
        video_dic = result['data']['resource']['progressive'][1]

        # 视频链接
        video = video_dic['url']
        # 视频格式
        video_fromat = video_dic['mime']

        xpc_item['video'] = video
        xpc_item['video_format'] = video_fromat

        yield xpc_item
