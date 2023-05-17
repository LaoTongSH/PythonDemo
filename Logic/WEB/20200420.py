# !-- coding:utf-8 --!
# !Code.Logic: 基础及爬虫 实训一  例題 01.1   2020年票房
# !@File:Code\Logic\WEB\ 20200420.py
# !@Author: Daisy
# !@Time:2020/4/21--11:40

import requests
import re
from bs4 import BeautifulSoup

html = requests.get('http://58921.com/alltime/2020')    # 实例对象用 get() 获取网页
html.encoding = 'utf-8'     # 执行支持汉化编码
html = html.text            # 把网页文本赋值给变量
#print(html)

# 正则 .*? 匹配电影名称
req = r'<td><a href="/film/.*?" title="(.*?)">.*?</a></td>'
title = re.findall(req,html)
#print(title)

# 用 BeautifulSoup 爬取网页，参数：源码，解析方式 或‘lxml’
soup = BeautifulSoup(html,'html.parser')
img_url = soup.find_all('img')[1:]
print(img_url)

i = 0
for url in img_url:             # 遍歷列表
    img_src = url.get('src')    # 獲取 src 部分數據
    img_content = requests.get(img_src).content     # 獲取圖片的二進制數據

    # 上下文管理器 with open() as f
    with open('Results/{}.png'.format(title[i]),'wb') as f:
        f.write(img_content)
    i += 1


