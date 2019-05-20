#-*- coding:utf-8 -*-
"""
Created on Wed May  8 17:19:38 2019

@author: zhangwenhao
"""

import requests as rqs #导入requests包
import time,csv,random,re
import numpy as np
from lxml import etree
#open函数记得加上encoding='utf-8'
with open('wandoujiat.csv','w',newline='',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    for i in range(2,200): #网页循环爬取不包含最后一页记得带冒号,小米官网只能15页15页爬：
        sleep = np.random.randint(3,6)  #导入时间包为爬虫增设延时爬取机制
        time.sleep(sleep)
        url = 'https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=0&ctoken=XovPYgIBgAYbi9_vB6maavKg&page=' + str(i) #所需爬取的网站链接
		#此处添加headers伪装成浏览器获取信息
        headers=[{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'},
				 {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'},
				 {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}]
		#此处构建IP池为爬虫脚本增设代理避免IP被封，IP池中的IP可从网上搜免费代理IP或导入开源IP池
        proxies=[{ "http":"117.191.11.106:80"},
                 {"http":"223.99.212.110:63000"},
                 {"http":"175.23.18.238:8080"},
                 {"http":"120.194.18.90:81"},
                 {"http":"175.155.138.168:1133"}] 
        strhtml = rqs.get(url, proxies=random.choice(proxies), headers=random.choice(headers), timeout=8)  #Get方式获取网页数据
        html = etree.HTML(strhtml.text)
        result = html.xpath('//li/a//@data-app-name')
        data=" ".join(result)
        par=re.compile("\"([^\"]*)\"")
        datas = par.findall(data)
        if not result == '':      
               writer.writerow(datas)    #导出爬取数据
        else:
            print(u'该类别已下载完最后一页')
  
            break	

