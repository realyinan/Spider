# 爬取51job全部城市岗位，并分别保存到单独的以城市名为文件名的html中，如: 深圳.html
# url = "https://jobs.51job.com/"
import requests
from bs4 import BeautifulSoup
import time
from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cookie': 'guid=38bbd4213b189d6d13b94ce4dff07487; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f7b7c14b415c8-01b760fdf696b87-26001d51-1327104-18f7b7c14b5a93%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmN2I3YzE0YjQxNWM4LTAxYjc2MGZkZjY5NmI4Ny0yNjAwMWQ1MS0xMzI3MTA0LTE4ZjdiN2MxNGI1YTkzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f7b7c14b415c8-01b760fdf696b87-26001d51-1327104-18f7b7c14b5a93%22%7D; acw_tc=ac11000117158264891501392e02bc619aa1740bdb38c097f4651b6c9e1ef3; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1715826488; jobs_search_req=0f3d6e0a6006631d05cd06492055b242; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1715826538; tfstk=fFzM7PfFYlo6_5OAIy018W_wQDIL1dgjV-LxHqHVYvkQMAIjBkYEMRHOGSW_nrDE7mZtHAHmoSwl9TQRy5Nsl0WReaecT_cqlx7xuhoDWiuVeTQdy5NslqrYfVEAWWkIijlq3-lF8bDE_CyqQDJEZbgq3-uVtWlWQGk_uyzFw8nQRH8pJycNhYPiKXGQ-fmiUaMHu5UnscDz6P_yt9cUJym-vIBn87ZLQX0lSLGgY70Zir1ymxm052c0AOxTERG4TD2OMnG3mSzS54AV7W0iI0zEfZf7UWV42D4daagi7Arx5SdlBW4gB5a3MI-ESVEnqP0PPdkYv74mir6f-8V4Noo3odjrcH-yF5LjTsUecniZOXD5LuHrBE74WYfht35jbXGse6fHcniZOXDRt6xPlclI1YC..; ssxmod_itna=YqGxgQ0QDtiQn4iq0L7k9DynDcjKD902merQxF+x0HyeGzDAxn40iDt==56CFQ0xbIaxTGOeAadDPEPRaObi7cnTWDCPGnDBF+xT3QxiiyDCeDIDWeDiDG4Gm94GtDpxG=Djjtz1M6xYPDEj5DRpPDuxBGDGP1LaKhDeKD0PTFDQ9hUrDDBr0veexY+xRGDiWFebypRpGE=n08D7yhDlP5cb08T8dUeAvEU4kGLWKDXOQDvOvw21oDUBKsyPY7==DP/j0eCnb4=jGxImDT7Y8NdPbKTYaq+DrB70UleDDWNCxY7YD===; ssxmod_itna2=YqGxgQ0QDtiQn4iq0L7k9DynDcjKD902merQxF4nIf2xDsOCGDLDUmrHe6j0Z4ApYnBikr0eeEpoBD8q=GlE2G=IReAav5oAw89ErxMjxAH1c9BQ=LQrLT=B9Ly9mFywwVbzNA8GTimK+A3LR3ouR8AjRxLKQGKGK0flK7rPArQdwCu3TbRhfniQPpT3k8Wl8SX49kxtq6EHpjtiwjhHcC2RFfovRfAlzl9TuSX5/4yYsaBNqUfUDSOGGeAmRd5LV+cQq8Fv03M+dbaGz6Bm3y3cXw6wKCWYseec+9fRfv=+z2xto0fW7GlhIGWeh7w4KEmYKqtejlv7xmVC6GD26PoAWrQz2q+6=KU=Ivfae2m6Y8rjn0Xlo33EiKmPP2sadFU5PIjHK6F/dbFpH4IqSI=3Kqg0cBb+/rsf=UCLUETfDah4IIRnpIrAFIwF5MPatcLUKpUFa06nF8A+h9QE4DQIKC2diK5KxkAMkoiC6RCTb5BLx+b4S45KbGLhYbDTbGzoQxfhx/rGH4=iCtWi4KG5zh+pQpOTq8DDFqD+rDxD'
}

def get_citys(url):
    # 获取网页数据

    response = requests.get(url, headers=headers)
    content = response.content.decode('gbk')
    print(content)

    soup = BeautifulSoup(content, features='lxml')
    a_list = soup.select('.lkst')[0].select('a')
    for a in a_list:
        name = a.text  # 城市名
        href = a['href']
        # print(name, href)
        get_job(href, name)
        time.sleep(2)


    

# 获取每个城市的岗位信息
def get_job(url, name):
    response = requests.get(url, headers=headers)
    content = response.content.decode('gbk')
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    div_list = soup.select('.detlist div')
    for div in div_list:
        title = div.select('.title a')[0].text
        print(f"{name}: {title}")


if __name__ == '__main__':
    url = "https://jobs.51job.com/"
    get_citys(url)