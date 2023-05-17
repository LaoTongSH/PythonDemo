# !-- coding:utf-8 --!
# !Code.Logic: 爬取小说    例題 05.1 不打开浏览器爬取起点网小说
# !@File:Code\Logic\WEB\ W20200512.1.py
# !@Author:
# !@Time:2020/5/12--9:04

import requests
import random
from lxml import etree

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
#    print(u_list[random.randint(0,len(u_list)-1)])     # 获取任意  User-Agent 方法
#    print(random.choice(u_list))                       # 同上，本法简单。
    return random.choice(u_list)    # 返回值：随机浏览器的 User-Agent
#random_user_agent()     # 调试用代码，调用  User-Agent 方法

def get_content():      # 获取内容函数
    url = "https://read.qidian.com/hankread/3144877/8478272"
    header = {
        "User-Agent":random_user_agent(),
        "Referer": "https://read.qidian.com/chapter/ozgK2uJ6kuk1/WD3xCwswdmr6ItTi_ILQ7A2",
        "Cookie": "_csrfToken=9vVONPMy9iJWMkAU2V27gAKdwm8qz5hB68RyRvTS; newstatisticUUID=1589252354_1026117159; e2=; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D; qdrs=0%7C3%7C0%7C1%7C1; showSectionCommentGuide=1; qdgd=1; lrbc=3144877%7C486663874%7C0; rcr=3144877; bc=3144877"
    }

    text = requests.get(url,headers=header).text    # 如无.text，获得的是 http 的状态码。
#    print(text)                 # 调试用代码，输出网页源码
    html = etree.HTML(text)
    # XPath 定位到文章的标题和内容
    titles = html.xpath("//div[@class='main-text-wrap']/div/h3/span[@class='content-wrap']/text()")
#    print(titles)               # 调试用代码,输出文章标题列表
    contents = html.xpath("//div[@class='main-text-wrap']/div/p/text()")
#    print(len(contents))        # 调试用代码，获取列表的元素数量
#    print(contents)             # 调试用代码，查看列表的元素特点，以便处理成每一章节为一个元素。
    contents = "".join(contents).split("              ")    # 列表的拼接和切片
    print(contents)             # 调试用代码，输出文章列表

    # for title,content in zip(titles,contents):      # 遍历文章标题、文章
    #     print(title)                                # 输出文章标题
    #     print(content)                              # 输出文章内容
    #
    #     with open('./Qidian/%s.txt'%title, 'w',encoding='utf-8') as file:
    #         file.write(content)                     # 上下文管理方法保存

# main
get_content()   # 调用获取内容函数


