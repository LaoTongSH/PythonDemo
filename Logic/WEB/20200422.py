# !-- coding:utf-8 --!
# !Code.Logic: python 实训二  例題 02.1  打开浏览器
# !@File:Code\Logic\WEB\ 20200422.py
# !@Author:Daisy
# !@Time:2020/4/22--21:42

from selenium import webdriver  # 导入selenium模块
driver = webdriver.Chrome()     # 打开浏览器
driver.implicitly_wait(20)      # 隐式等待20秒
driver.maximize_window()        # 窗口最大化
driver.get('https://www.baidu.com/')    # 使用get方法获取网站

# 使用 id 定位到搜索框
search_field = driver.find_element_by_id('kw')

# # 使用 name 定位到搜索框
# search_field = driver.find_element_by_name('wd')
# # 使用 class.name 定位到搜索框
# search_field = driver.find_element_by_class_name('s_ipt')

search_field.clear()                # 清空列表
search_field.send_keys('pygame')    # 赋值，输入 pygame 进行搜索
search_field.submit()               # 提交

# '//*[@srcid=1599]'可以直接在浏览器中使用开发者工具查找定位
products = driver.find_elements_by_xpath('//*[@srcid=1599]')
# 获取元素数量及值
print ('共找到 ' + str(len(products)) + ' 个结果:')
n = 1
for product in products:                # 使用循环进行遍历
    print ('No',n,':',product.text)    # 输出结果
    n += 1

#driver.quit()               # 关闭浏览器窗口






