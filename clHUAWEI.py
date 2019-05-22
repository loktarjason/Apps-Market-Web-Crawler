# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:33:39 2019
@author: loktarjason
"""

import requests as rqs #导入requests包
from bs4 import BeautifulSoup #导入bs4用于提取网页数据
import time, csv 
with open('huaweiSHOP.csv', 'w', newline='',encoding='utf-8-sig') as f: #在爬取数据的循环之前，先打开存数据的文件，提高效率
    writer = csv.writer(f)                #定义写入打开存数据的文件函数
    time.sleep(3)                         #导入时间包为爬虫增设延时爬取机制
    for i in range(1,10):                 #网页循环爬取不包含第40页记得带冒号：
        url = 'http://appstore.huawei.com/soft/list_358_1_' + str(i) #所需爬取的网站链接
        #此处添加headers伪装成浏览器获取信息
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        proxies={ "http":"http://121.8.98.196:80"} #此处构建IP池为爬虫脚本增设代理避免IP被封,假死注意监测代理IP有效性
        strhtml = rqs.get(url,proxies=proxies,headers=headers,timeout=8)  #Get方式获取网页数据，设置timeout用于防止假死
        strhtml.encoding = 'utf-8' #将获取结果转码可识别中文
        soup=BeautifulSoup(strhtml.text, 'lxml') #调取bs4中的网页解析函数.text代表网页源码
        data = soup.select('body > div.lay-body > div.lay-main > div.lay-left.corner > div.unit.nofloat.prsnRe > div.unit-main > div > div.game-info.whole > h4 > a') #抓取特定网页sector的所有类似sector数据
        a_text = [c.get_text()for c in data] #提取爬取数据中的文字text
        writer.writerow(a_text) #输出

