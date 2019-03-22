#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : BigC
# @Email   : big_it@126.com
# @File    : 简历采集.py
# @Software: PyCharm
import requests
import random
from lxml import etree
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
                  'Connection':'close'
}
# 'Connection': 'close' 连接成功之后之后断开
first_url='http://sc.chinaz.com/jianli/free.html'
current_url='http://sc.chinaz.com/jianli/free_%s.html'
start_num=int(input("请输入起始页码"))
end_num=int(input("请输入终止页码"))
# if start_num==1 and end_num==1:
#     url=first_url
for page_num in range(start_num,end_num+1):
    if page_num==1:
        url=first_url
    else:
        url = current_url%page_num
    page_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)
    a_lidst = tree.xpath('//div[@id="container"]/div/a/@href')
    # print(len(a_lidst),a_lidst)
    for deatail_url in a_lidst:
        detai=requests.get(url=deatail_url,headers=headers)
        detai.encoding='utf-8'
        tree=etree.HTML(detai.text)
        name=tree.xpath('//div[@class="bread clearfix"]//a[3]/text()')[0]

        download_url_list = tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li')
        # print(download_url_list)
        li=random.choice(download_url_list)
        download_url = li.xpath('./a/@href')[0]
        print(download_url)
        data=requests.get(url=download_url,headers=headers).content
        # name=name+'.rar'
        # print(name)
        # with open(name,'wb') as fp:
        #     fp.write(data)
        # print(name,'下载完毕')
        name = name + '.rar'
        with open(name, 'wb') as fp:
            fp.write(data)
        print(name, '下载成功！')

print('done')