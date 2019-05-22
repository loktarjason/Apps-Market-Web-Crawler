# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:35:54 2019

@author: loktarjason
"""
import requests as rqs #导入requests包
from bs4 import BeautifulSoup
import time,json,csv
with open('miSHOP9.csv', 'w', newline='',encoding='utf-8') as f: #open函数记得加上encoding='utf-8'
    writer = csv.writer(f)
    for i in range(0,15): #网页循环爬取
        time.sleep(3)  #导入时间包为爬虫增设延时爬取机制
        url = 'http://app.mi.com/categotyAllListApi?categoryId=9&pageSize=30&page=' + str(i) #所需爬取的网站链接
        #此处添加headers伪装成浏览器获取信息
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
		
        proxies=[{ "http":"117.191.11.106:80"}] #此处构建IP池为爬虫脚本增设代理避免IP被封，IP池中的IP可从网上搜免费代理IP或导入开源IP池
		
        strhtml = rqs.get(url,proxies=random.choice(proxies),headers=headers,timeout=8)  #Get方式获取网页数据
        #strhtml.encoding = 'utf-8' #将获取结果转码可识别中文
        soup=BeautifulSoup(strhtml.text, 'lxml') #调取bs4中的网页解析函数.text代表网页源码
        a_text = [c.get_text()for c in soup] #提取爬取数据中的文字text
        l_text = "".join(a_text) #将爬取的数据转为str
        data = json.loads(l_text) #将str转为json
        apps = data['data'] #处理json数据截取所需的数据区间
        for n in apps:
            apps = n['displayName']       
            apps_list = apps.split() #数据转为lis存储易于使用
            writer.writerow(apps_list)    #导出爬取数据