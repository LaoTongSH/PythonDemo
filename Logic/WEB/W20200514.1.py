# !-- coding:utf-8 --!
# !Code.Logic: 爬取小说    例題 05.2 不打开浏览器批量爬取起点网小说
# !@File:Code\Logic\WEB\ W20200514.1.py
# !@Author: LaoTong
# !@Time:2020/5/14--12:00

import requests
import random
from lxml import etree
import os

def random_user_agent():            # 随机选取常见浏览器 User-Agent 方法
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
    return random.choice(u_list)    # 返回值：随机浏览器的 User-Agent

def get_content(table,url):         # 获取内容函数
    header = {
        "User-Agent":random_user_agent(),
        "Referer": "https://book.qidian.com/info/3144877",
        "Cookie": "_csrfToken=9vVONPMy9iJWMkAU2V27gAKdwm8qz5hB68RyRvTS; newstatisticUUID=1589252354_1026117159; e2=; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D; qdrs=0%7C3%7C0%7C1%7C1; showSectionCommentGuide=1; qdgd=1; lrbc=3144877%7C486663874%7C0; rcr=3144877; bc=3144877"
    }

    mypath = os.path.join('./Qidian/',table)    # 连接成路径目录
    if not os.path.exists(mypath):              # 判断目录存在
        os.makedirs(mypath)                     # 创建目录
#    print("w:/",mypath)                        # 调试用代码，输出路径目录名称

    text = requests.get(url).text       # 如无.text，获得的是 http 的状态码。
    html = etree.HTML(text)             # 转换成 Lxml 语言，便于定位。

    # XPath 定位到文章的标题和内容
    titles = html.xpath("//div[@class='main-text-wrap']/div/h3/span[@class='content-wrap']/text()")
    contents = html.xpath("//div[@class='main-text-wrap']/div/p/text()")
    contents = "".join(contents).split("              ")    # 文章列表的拼接和切片

    for title,content in zip(titles,contents):              # 遍历文章标题、文章
        mypaths = os.path.join(mypath,"%s.txt"%title)       # 连接成路径、目录、文件名

        with open(mypaths, 'w',encoding='utf-8') as file:
            file.write(content)                             # 上下文管理方法保存

# main
# 创建 卷连接列表和卷名称列表
urls = (
    "https://read.qidian.com/hankread/3144877/8478272",
    "https://read.qidian.com/hankread/3144877/8531801",
    "https://read.qidian.com/hankread/3144877/8803523",
    "https://read.qidian.com/hankread/3144877/9318826",
    "https://read.qidian.com/hankread/3144877/9805659"
)
tables = ("01.初来乍到·共18章","02.踏上征途·共89章","03.无尽星空·共141章","04.星空百族·共150章","05.起源大陆·共171章")

for table,url in zip(tables,urls):  # 遍历卷名称、连接列表
    get_content(table,url)          # 调用按卷获取内容函数

