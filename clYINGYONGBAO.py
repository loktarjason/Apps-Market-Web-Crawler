# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:33:39 2019
@author: loktarjason
"""

import requests as rqs #导入requests包
from bs4 import BeautifulSoup
import time, csv, json
with open('yingyongbaoFIN2.csv', 'w', newline='',encoding='utf_8_sig') as g: #encoding='utf_8_sig'，防止中文乱码
   writers = csv.writer(g)
   for i in (40,47,74,96): #网页循环爬取,YINGYONGBAO由于数据页面并非按顺序排列
       time.sleep(3)  #导入时间包为爬虫增设延时爬取机制
       url = 'https://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId=114&pageSize=20&pageContext=' + str(i) #所需爬取的网站链接
       headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
       proxies={ "http":"120.198.230.15:8080"} #此处构建IP池为爬虫脚本增设代理避免IP被封，IP池中的IP可从网上搜免费代理IP或导入开源IP池
       strhtml = rqs.get(url,proxies=proxies,headers=headers,timeout=8)  #Get方式获取网页数据
       soup=BeautifulSoup(strhtml.text, 'lxml') #调取bs4中的网页解析函数.text代表网页源码
       a_texts = [c.get_text()for c in soup] #提取爬取数据中的文字text
       l_text = "".join(a_texts) #将爬取的数据转为str
       datas = json.loads(l_text) #将str转为json
       apps = datas['obj'] #处理json数据截取所需的数据区间
       for n in apps:
           apps = n['appName']       
           apps_list = apps.split() #数据转为lis存储易于使用
           writers.writerow(apps_list)    #导出爬取数据