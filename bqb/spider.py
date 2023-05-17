#encoding: utf-8

import requests
from bs4 import BeautifulSoup
from urllib import request
import os
import threading

# 首先先要对请求的身份进行伪装。
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

# 用来存储所有的页面的url
PAGE_URLS = []
IMG_URLS = []
gLock = threading.Lock()

# 生产者：专门用来获取表情包的url链接。
# 消费者：专门从表情包的url链接中下载图片
# 全局变量：就是一个列表，这个列表存储了许多的表情包的链接。

def producer():
    while True:
        gLock.acquire()
        if len(PAGE_URLS) == 0:
            gLock.release()
            break
        page_url = PAGE_URLS.pop()
        gLock.release()
        response = requests.get(page_url, headers=headers)
        text = response.text
        soup = BeautifulSoup(text, 'lxml')
        img_list = soup.find_all("img", attrs={"class": "img-responsive lazy image_dta"})
        for img in img_list:
            # 有些img_url没有http前缀
            img_url = img['data-original']
            IMG_URLS.append(img_url)

def consumer():
    while True:
        gLock.acquire()
        if len(IMG_URLS) == 0 and len(PAGE_URLS) == 0:
            gLock.release()
            break
        if len(IMG_URLS) > 0:
            img_url = IMG_URLS.pop()
        else:
            img_url = ''
        gLock.release()
        # https://ws2.sinaimg.cn/bmiddle/9150e4e5gy1g0saavmreuj20250250sh.jpg
        # ['https:','','ws2.sinaimg.cn','bmiddle','9150e4e5gy1g0saavmreuj20250250sh.jpg']
        # windows: D:\PublicCourse\class\2019_03_06\bqb
        # Mac/Linux/Unix：/root/srv
        if img_url:
            try:
                filename = img_url.split("/")[-1]
                fullpath = os.path.join("images", filename)
                request.urlretrieve(img_url, fullpath)
                print("%s下载完成" % filename)
            except:
                print("="*30)
                print(img_url)
                print("=" * 30)

def main():
    # 1. 先获取所有页面的url
    for x in range(1,100):
        page_url = "https://www.doutula.com/photo/list/?page="+str(x)
        PAGE_URLS.append(page_url)

    # 五个生产者线程
    for x in range(5):
        th = threading.Thread(target=producer)
        th.start()

    # 五个消费者线程
    for x in range(5):
        th = threading.Thread(target=consumer)
        th.start()

if __name__ == '__main__':
    main()
