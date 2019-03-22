#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : BigC
# @Email   : big_it@126.com
# @File    : xpath的与位运算.py
# @Software: PyCharm
import requests
import random
from lxml import etree
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
                  'Connection':'close'
}
url='https://www.aqistudy.cn/historydata/'
page_text=requests.get(url=url,headers=headers,).text
tree=etree.HTML(page_text)
all_city_list=tree.xpath('//div[@class="hot"]/div[@class="bottom"]/ul/li/a/text() | //div[@class="all"]/div[@class="bottom"]/ul//div[2]/li/a/text()')
print(len(all_city_list),all_city_list)