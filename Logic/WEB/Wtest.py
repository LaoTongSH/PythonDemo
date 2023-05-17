# !-- coding:utf-8 --!
# !Code.Logic: 爬取 mp3  例题 06.1  爬取千千音乐网站
# !@File:Code\Logic\WEB\ Wtest.py
# !@Author: LaoTong
# !@Time:2020/5/14--22:38

import datetime
now = datetime.datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))


from selenium import webdriver  # 导入selenium模块
driver = webdriver.Chrome()     # 打开浏览器
driver.implicitly_wait(20)      # 隐式等待20秒
driver.maximize_window()        # 窗口最大化
driver.get('http://data.eastmoney.com/zjlx/600480.html')    # 使用get方法获取网站

products = driver.find_elements_by_xpath('//table[@id="dt_1"]/tbody')

#print(products)
for product in products:                # 使用循环进行遍历
    print (product.text)
driver.quit()               # 关闭浏览器窗口














'''
# import os

path = os.getcwd()
print(path)
img_dir = "table"
os.makedirs('./Qidian/'+img_dir)

# test 01
import requests

url = "http://audio04.dmhmusic.com/71_53_T10046690552_128_4_1_0_sdk-cpm/cn/0210/M00/6F/08/ChR461t_jnGAJIK0ADPI4UNR_-E884.mp3?xcode=c04e6d0e4e008f8d6610a641dad133dc4b75473"

result = requests.get(url).content

with open("./1233.mp3","wb") as f:
    f.write(result)

# test 03
import requests
import json

play_url = "http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.play&songid" \
          "=672865438"
result = requests.get(play_url).text            # 对 play_url 发出请求
# print(result)                                   # 输出获取的数据 是 ison 格式
# print("*"*80)
result = json.loads(result)                     # 列表数据
# print(result)                                   # 输出反转换成 Python 格式的数据
dict_url = result['bitrate']['file_link']               # 正则定位筛选,获取歌曲下载连接
# print(dict_url)
dict_txt = requests.get(dict_url).content      # 对连接发出请求，获取二进制数据

with open("./1233.mp3","wb") as f:
    f.write(dict_txt)

'''





