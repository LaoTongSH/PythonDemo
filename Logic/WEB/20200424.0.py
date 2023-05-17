# !-- coding:utf-8 --!
# !Code.Logic: 电影抓取，  例题 03.1   抓取予告片
# !@File:Code\Logic\WEB\ 20200424.0.py
# !@Author:James
# !@Time:2020/4/24--23:07

import requests             # 导入框架
from lxml import etree      # 导入 lxml 模块
import re

# 添加浏览器特征码，反反爬
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/81.0.4044.122 Safari/537.36'
}

url = ' https://maoyan.com/news?showTab=3'                   # 创建页面链接列表
result = requests.get(url,headers = header).content.decode() # 获取自动解码的数据
#print(result)

dom = etree.HTML(result)    # 转换成 LXML 语言
movie_names = dom.xpath('//h4[@class="video-name one-line"]/a[@href]/text()')   # 用 XPath 筛选出电影名称列表
movie_urls = dom.xpath('//h4[@class="video-name one-line"]/a[@href]/@href')     # 用 XPath 筛选出电影连接列表

for movie_name,movie_url in zip(movie_names,movie_urls):    # 遍历二个列表
    movie_name = movie_name.split('》')[0]                  # 切去多余的字符串
    # print(movie_name[1:])
    # print(movie_url)

    movie_id_sting = requests.get(movie_url).text           # 获取电影连接的文本数据
    mp4_url = re.search('source src="(.*?)"',movie_id_sting).group(1)   # 用正则筛选，group() 参数值：空，0，1
#    print(mp4_url)
    mp4 = requests.get(mp4_url).content     # 获取二进制的文件

    # 上下文管理器 with open() as file
    with open('./movieResults/%s.mp4'%movie_name[1:],'wb') as file:
        file.write(mp4)                     # 下载视频，生成文件

































































# __author__ = 'Eagle'
# # 163 邮件登录器
# #前提pip install webdriver
# from selenium import webdriver
# #打开火狐浏览器
# driver = webdriver.Chrome()     # 打开浏览器
# #打开163
# driver.get("http://mail.163.com/")
# #设置全屏
# driver.maximize_window()
#
# ##输入账号密码
# driver.find_element_by_id("lbNormal").click()
# #输入账号 163 账号
# driver.find_element_by_name("email").send_keys("laotong")      #切记不带@163.com
# #输入密码163 密码
# driver.find_element_by_id("pwdInput").send_keys(r"password")   #输入密码
# ###点击登录按钮
# driver.find_element_by_id("loginBtn").click()