# !-- coding:utf-8 --!
# !Code.Logic: 爬取壁纸    例題 04.1 爬取回车壁纸
# !@File:Code\Logic\WEB\ W20200508.1.py
# !@Author:
# !@Time:2020/5/8--10:39

import time
from selenium import webdriver  # 导入selenium模块
from selenium.webdriver.support.ui import WebDriverWait             # 等待驱动
from selenium.webdriver.support import expected_conditions as EC    # 预期条件
from selenium.webdriver.common.by import By                         # 构造条件的模块
import requests                                                     # 导入模块
import os                       # 导入系统模块

driver = webdriver.Chrome()     # 打开浏览器
driver.implicitly_wait(10)      # 隐式等待10秒

def get_html():                 # 定义获取网站数据函数。最后返回数据列表
    url = "https://www.enterdesk.com/zhuomianbizhi/fengjing/"       # 定义网站链接变量
    driver.get(url = url)       # 获取网站
    driver.implicitly_wait(10)  # 隐式登待
    # 显示等待，隔0.5秒检测，共10秒，元素加载完成后，停止等待。过时报错。
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((
        By.CSS_SELECTOR,".egeli_pic_m")))

    # 用 CSS 选择器，定位到父级类标签元素。
    pic_m = driver.find_element(By.CSS_SELECTOR,'.egeli_pic_m')
    # 用 CSS 选择器，定位到子级标签元素 img
    img_li = pic_m.find_elements(By.CSS_SELECTOR,'.egeli_pic_li dl dd a img')
#    print(img_li)
    # 数据筛选
    li = []
    for img in img_li:
        img_info = {}
        img_info["img_url"] = img.get_attribute('src')
        img_info["img_title"] = img.get_attribute('title')
        li.append(img_info)
#    print(li)
    return li

def save(img_info_list):            # 定义存储图片函数
    img_dir = "Enterdesk"           # 设置图片存蓄目录
    if not os.path.exists(img_dir): # 判断目录存在
        os.makedirs(img_dir)        # 创建目录

    for img in img_info_list:
        img_con = requests.get(url=img['img_url']).content  # 从连接获取图片二进制文件
        img_path = os.path.join(img_dir,img['img_title']+'.jpg')    # 创建图片路径文件名

        # 上下文管理器 with open() as file
        with open(img_path,'wb') as file:
            file.write(img_con)                    # 下载图片，生成文件
        print(f"正在保存：{img['img_title']}")       #  用 f 格式
# main
img_info_list = get_html()
save(img_info_list)
driver.quit()


