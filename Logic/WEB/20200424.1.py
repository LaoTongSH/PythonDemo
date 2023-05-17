# !-- coding:utf-8 --!
# !Code.Logic: 电影抓取 增强版 抓取多页预告片
# !@File:Code\Logic\WEB\ 20200424.1.py
# !@Author:James-LaoTong
# !@Time:2020/4/29--18:40

import requests             # 导入框架
from lxml import etree      # 导入 lxml 模块
import re

# 添加浏览器特征码，反反爬
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
# 创建页面链接列表
urls =['https://maoyan.com/news?showTab=3&offset=0','https://maoyan.com/news?showTab=3&offset=16',
       'https://maoyan.com/news?showTab=3&offset=32','https://maoyan.com/news?showTab=3&offset=48'
]

for url in urls:    # 遍历链接列表
    result = requests.get(url, headers=header).content.decode()  # 获取自动解码的数据

    dom = etree.HTML(result)  # 转换成 LXML 语言
    movie_names = dom.xpath('//h4[@class="video-name one-line"]/a[@href]/text()')  # 用 XPath 筛选出电影名称列表
    movie_urls = dom.xpath('//h4[@class="video-name one-line"]/a[@href]/@href')  # 用 XPath 筛选出电影连接列表
    for movie_name, movie_url in zip(movie_names, movie_urls):  # 遍历二个列表
        movie_name = movie_name.split('》')[0]  # 切去多余的字符串
        # print(movie_name[1:])
        # print(movie_url)

        movie_id_sting = requests.get(movie_url).text  # 获取电影连接的文本数据
        mp4_url = re.search('source src="(.*?)"', movie_id_sting).group(1)  # 用正则筛选，group() 参数值：空，0，1
        mp4 = requests.get(mp4_url).content

        # 上下文管理器 with open() as file
        with open('./movieResults/%s.mp4' % movie_name[1:], 'wb') as file:
            file.write(mp4)
