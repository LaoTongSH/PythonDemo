# !-- coding:utf-8 --!
# !Code.Logic: 爬取 mp3  例题 06.2  爬取千千音乐网站
# !@File:Code\Logic\WEB\ W20200517.1.py
# !@Author: LaoTong
# !@Time:2020/5/17--12:05

import requests
from lxml import etree
import random
import time
import json
import os

home_url = "http://music.taihe.com"     # 首页网址
top_url = "http://music.taihe.com/top"  # top 页面链接
# 播放单曲页面
play_url = "http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid="

if not os.path.exists("./Baidumusic"):  # 判断目录存在，创建目录
    os.makedirs("./Baidumusic")
print("下载总目录创建完成！","\n")

def random_user_agent():                # 随机选取常见浏览器 User-Agent 方法
    u_list = [
        "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
        "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    ]
    return random.choice(u_list)        # 返回值：随机浏览器的 User-Agent

# 反爬三件套
header = {
    "User-Agent":random_user_agent(),
    "Referer": "https://book.qidian.com/info/3144877",
    "Cookie": "_csrfToken=9vVONPMy9iJWMkAU2V27gAKdwm8qz5hB68RyRvTS; newstatisticUUID=1589252354_1026117159; e2=; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D; qdrs=0%7C3%7C0%7C1%7C1; showSectionCommentGuide=1; qdgd=1; lrbc=3144877%7C486663874%7C0; rcr=3144877; bc=3144877"
}

# # 发起请求，获取 源码纯文本--会乱码。
# song_text = requests.get(url,headers=header).text

# 对 top 页面发起请求，获取榜单数据(字节为单位.编码规则)
song_text = requests.get(top_url,headers=header).content.decode()
time.sleep(0.1)                                         # 等待

# 数据筛选定位，获取榜单名称和链接二个列表
song_dom = etree.HTML(song_text)                        # HTML 转换成 Lxml
song_ids = song_dom.xpath("//dd/a[@href]/@href")[:-2]   # XPath + 切片
song_names = song_dom.xpath("//dd/a[@href]/text()")[:-2]
print("歌曲榜单列表创建完成！","\n")

for song_id,song_name in zip(song_ids,song_names):      # 遍历榜单的二个列表
    song_url = home_url + song_id                       # 拼接成 榜单 List 页面的地址
    time.sleep(1)                                       # 等待

    # 对 榜单 List 页面发出请求，获取歌曲数据(字节为单位.编码规则)
    sub_text = requests.get(song_url,headers=header).content.decode()

    # 数据筛选定位，获取榜单 List 中歌曲的名称和播放链接二个列表
    sub_dom = etree.HTML(sub_text)                      # HTML 转换成 Lxml
    sub_ids = sub_dom.xpath("//a[contains(@href,'/song/')]/@href")[1:]
    sub_names = sub_dom.xpath("//a[contains(@href,'/song/')]/text()")[1:]

    mypath = os.path.join('./Baidumusic/', song_name)   # 连接成路径目录
    if not os.path.exists(mypath):                      # 判断目录存在
        os.makedirs(mypath)                             # 目录不存在，创建

    print("*"*30)
    print(song_name," 子目录创建完成，共有歌曲", len(sub_names), "首。")
    print("*"*30,"\n")

    # 遍历分类榜单 List 列表，获取单曲的名称和下载连接
    for sub_id,sub_name in zip(sub_ids,sub_names):
        sub_id = sub_id.split('/')[2]                   # 切片，获取纯 ID
        sub_url = play_url+sub_id                       # 拼接成歌曲的播放连接
        print("歌曲：《",sub_name," 》下载准备完成！")

        sub_song_url = requests.get(sub_url,headers=header).text    # 对 play_url 发出请求
        sub_song_url = json.loads(sub_song_url)                     # 转换成 python 格式
        try:
            dict_url = sub_song_url['bitrate']['file_link']         # 正则定位筛选,获取歌曲下载连接
        except KeyError:
            print("歌曲：《", sub_name, " 》解析出错！")
            print("*"*40,"\n")
            exit()

        dict_txt = requests.get(dict_url).content                   # 对连接发出请求，获取二进制数据

        mypathfile = os.path.join(mypath,"%s.mp3"%sub_name)         # 连接成路径、目录、文件名
        print("下载歌曲：",mypathfile," 进行中...")
        time.sleep(0.1)                                             # 等待

        try:
            with open(mypathfile, 'wb') as file:
                file.write(dict_txt)                                    # 上下文管理方法保存
            print("歌曲：《", sub_name, " 》下载成功！", "\n")
        except FileNotFoundError:
            print("歌曲：《", sub_name, " 》下载出错！")
            print("*"*40,"\n")

print("歌曲下载全部完成 ！！")



