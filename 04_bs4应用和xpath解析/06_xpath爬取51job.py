import requests
import time
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cookie': 'guid=38bbd4213b189d6d13b94ce4dff07487; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f7b7c14b415c8-01b760fdf696b87-26001d51-1327104-18f7b7c14b5a93%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmN2I3YzE0YjQxNWM4LTAxYjc2MGZkZjY5NmI4Ny0yNjAwMWQ1MS0xMzI3MTA0LTE4ZjdiN2MxNGI1YTkzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f7b7c14b415c8-01b760fdf696b87-26001d51-1327104-18f7b7c14b5a93%22%7D; acw_tc=ac11000117158468380045790e04b9b206b88c946aaf4ef07e6a3bc3a4be77; tfstk=fSpH7AiZ_B5Ih4r--dXIQY7R6MG9Ay65GUeRyTQr_N762wh5JC2N2eQKV3uBrLbNL_OdywQlE3TmXqHxHHtCFsuxkxpCIu25FakRUW5upbWrkqHtHHtCFTRJOo7Zph71qgSUTUSZQibNYz8P81zNmi6PzUWrjhlW3X7BUdJZDXAqiHPa_djEPZ-hSGs6IMfhux_gUBpGx6b2vpM4jVjwBdfA6u3GQnO98GXmKrsH_nXFqLi4ZafkdOjk12Vpoesyb1YK27sMZ3JfdtqrLhXh-sJNOYmXuhxyM1vt0x6hLwRRd3EmJhvHJH9M2uPNK9dGipXqhy7J6nvlqLgSIExycQ5MEyjrG5P4lHe5b0paN71FfGbj7IQVJ8kypZmijSo5TGsCkcmgN71FfGbxjcVqF6S1AZC..; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1715826488,1715846836; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1715846836; ssxmod_itna=eqmxgQ0=G=0Qi=w50dD=wEb40EU9i3=OdD0mx0vneGzDAxn40iDt=xH61bWblWUoxfswmn7xf=dfAS2rWo8W4cnT7DCPGnDBFq4TB=xiinDCeDIDWeDiDG4Gm94GtDpxG=Djjtz1M6xYPDEj5DRpPDuxBGDGP1LaKhDeKD0gbFDQ9hUa4DBaRvpBh7dQYDepPhn1EC=WSDqjKD91YDsZD6pj9mczkoSa8LXKY3px0kPq0O9g7CH4GdU2y1x4KTeW2eMj2eNAbqqjhxaWRr7NG5SAexdm0eb=04VjrBOm1ZpDDWqW4Ks=GDD=; ssxmod_itna2=eqmxgQ0=G=0Qi=w50dD=wEb40EU9i3=OdD0Dn9o2T4DsqaaDLlljoy=l3XFF3NAehbM/OAPxOD8OGQH=V6Ovxsn31QOn1Q1+COTEixKK7qqKmPT8bUNpZk0+1kQmiFql6/aEhQgVzANEBb+bIxmxPuPUDC0jArNGmgY42EPpIEN4fBb=M4To1m5da3o0UjEIAl2PPMYB/nWG8Z=bTc985jXTdaRhiaR4+jEe8D7Bbj9xF/R5=M7VGFW67mn5T9YAHlr4YAuXBhAfHjNUnPCrkLgCH5gcavdBsmRIm5C4/L9KefPKF8TGWhuD6BAwNjmKjhkiG=jGHadXEm5jmklGd6D3bfOAmkQAofeMB2pGK362tz2QtA=+IPZ2i/UT32p7va6mofRO/E=zuXEexcu/iER1Ad62sSTe/ENznNbWpG2zaRm3bMcLmOtEPo4rdL4QjKXWpN4o9mCcGz4DQ9q3rqmu/0xKTiqkR8kkd8D7+MC5qxD08DijbYD='
}

def get_citys(url):
    # 获取网页数据
    response = requests.get(url, headers=headers)
    content = response.content.decode('gbk')
    # print(content)

    # xpath解析
    mytree = etree.HTML(content)
    a_list = mytree.xpath('//*[@class="e e4"][1]/*[@class="lkst"][1]/a')

    for a in a_list:
        name = a.xpath("./text()")[0]
        href = a.xpath("./@href")[0]

        # print(name, href)

        get_job(href, name)


# 获取每个城市的岗位信息
def get_job(url, name):
    response = requests.get(url, headers=headers)
    content = response.content.decode('gbk')
    # print(content)

    # xpath解析
    mytree = etree.HTML(content)
    div_list = mytree.xpath('.//*[@class="detlist gbox"]/div')

    for div in div_list:
        # 岗位名称
        name = div.xpath('.//*[@class="title"]/a/text()')
        # 城市
        city = div.xpath('.//*[@class="location name"]/text()')
        # 薪资
        salary = div.xpath('.//*[@class="location"]/text()')
        # 学历
        degree = div.xpath('.//*[@class="order"]/text()')
        print(name, city, salary, degree)



if __name__ == '__main__':
    url = "https://jobs.51job.com/"
    get_citys(url)