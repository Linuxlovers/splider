#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : BigC
# @Email   : big_it@126.com
# @File    : 处理2.py
# @Software: PyCharm
import json

# 使用三引号将浏览器复制出来的requests headers参数赋值给一个变量
headers = """
accept-ranges: bytes
access-control-allow-origin: https://my.csdn.net
age: 1994898
ali-swift-global-savetime: 1543480667
cache-control: max-age=31104000
content-length: 13246
content-md5: MFkx2J9vBU71ssNE/W9V4Q==
content-type: image/jpeg
date: Wed, 27 Feb 2019 09:20:02 GMT
eagleid: 1bdd389c15532541001213670e
etag: "305931D89F6F054EF5B2C344FD6F55E1"
last-modified: Thu, 01 Feb 2018 10:15:59 GMT
server: Tengine
status: 200
timing-allow-origin: *
via: cache27.l2em21-1[0,200-0,H], cache30.l2em21-1[1,0], vcache17.cn646[0,200-0,H], vcache8.cn646[2,0]
x-cache: HIT TCP_HIT dirn:0:668131903
x-oss-hash-crc64ecma: 17297514400655391278
x-oss-object-type: Normal
x-oss-request-id: 5C765642DF97EB105C975555
x-oss-server-time: 49
x-oss-storage-class: Standard
x-swift-cachetime: 2592000
x-swift-savetime: Mon, 18 Mar 2019 07:22:40 GMT
:authority: avatar.csdn.net
:method: GET
:path: /A/9/F/3_qq_38251616.jpg
:scheme: https
accept: image/webp,image/apng,image/*,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: smidV2=201810171611197a8bb464e98c4f5aaf5463c5e4a44e8b0030b565d7f43d250; UN=weixin_43063753; UM_distinctid=1668b77eeca133-05f28b9ab677b9-551f3c12-100200-1668b77eecb48a; uuid_tt_dd=10_28867322930-1540625162019-930786; ARK_ID=JS298df331ccde3e6f3678c765e30bd4c8298d; CloudGuest=NEp9ejVBFVz0yJZvhojzGLQfR7F8jojqc8omF5Nbg3fSVjabYyo6qiOuOY6FHT03ib2gSPUkf3k/8i3qncJJ9CpYV1N07KpNUTglrxx7xFX21zrmxnlL+Gqms2kixwshxeTXSkUGoMV6ANd6Va33ItICbXMZTo683oMxNnaGR9BiCT3A1bb5BtWgVp0r/HjQ; OUTFOX_SEARCH_USER_ID_NCOO=1246435806.344866; _ga=GA1.2.736618063.1542085817; gr_user_id=29fa1d2a-dc82-4f75-a24f-df1eebe20181; _dg_id.40e39cb6d36d5282.c482=ef5b9670a467c64a%7C%7C%7C1547892923%7C%7C%7C1%7C%7C%7C1547892923%7C%7C%7C1547892923%7C%7C%7C%7C%7C%7Cd44ea87017817657%7C%7C%7Chttps%3A%2F%2Fwww.google.com.hk%2F%7C%7C%7Chttps%3A%2F%2Fwww.google.com.hk%2F%7C%7C%7C1%7C%7C%7Cundefined; pt_7cd998c4=uid=6YBnK0IESbbZNBT7GYC67w&nid=0&vid=5MJJt/3D8y0nlIq9x6ld1A&vn=2&pvn=1&sact=1547903151106&to_flag=0&pl=1lNgTuhYPyb3g-jHwKpQBA*pt*1547903147506; UserName=weixin_43063753; UserInfo=62b1618691b842328c7039d52dbdeb13; UserToken=62b1618691b842328c7039d52dbdeb13; UserNick=BigC%E5%93%A5; AU=FF7; BT=1551101901910; dc_session_id=10_1551704326283.464338; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!5744*1*weixin_43063753!6525*1*10_28867322930-1540625162019-930786; aliyun_webUmidToken=TC01A03D62EC8D7C9AB8C2913C2765B6BFC92D85E5BC8FAE84A4D8430C3; aliyun_UAToken=115#1XS2c11O1TNJiMhiTCCb1CsoE562CpA11g2mOCXwJ5OcAzdCoO0gQftuKX+fyze2xsfy9+/8y++hi/JJhUU4AkNca8pAurPQOSfyetT8ukZQgQkRhEPCOSgaCY9XuzFZASAyeKT8ukNQiFMJhUU4AWNcaBefyzFQOSRlTRDv5H6omDk5Ht5taR2QSFAFR0RLhpqbWeucFGadA9GaxoM3rQwgl18cAuKx1kEDrx2Tc6yeaNktr/odSfeGtkuB6dX18ccvvyl/L9JBNNb6Zyk5JjKmqno4c+pmfK5HDtM8O/WVWWGt8Gmoog+2ECW3nc4kWgIR1DUlb9MKmrP6gOjYEc7VMZYNVQD+u0HE6J2faU5Ar2n5x0nsKm1vgQoOUxc+vDW8IedFtcjAv137uIqiEtyzFqrNs92zt+dbfcJjethRTaHeOI96/kUwMvRVo3E45n0kPnhJjprKlqElJlu+/QuTXU8Zrc4BqA53wock1+IR6WXriXe7W+XPf4j9FWnXEzap4lJt5e5S7pyW219280ak2FtvWKcA48Ba5Lx+cpCar6+N/TETjwKiAvdd60z64pWsATADHLbfbvFJ6VV1g02uGkPd32d9brLxqIWEhrXMRb8zTF3kDpeLp6Yu4fWgjmiuW3e7AADoClX8DYXe5fJFeIqWB8PHWm+CtEB6SLPSbLxs5o18k36nw4sb6nkGcwpUkZDuj0QC+B/kolhQ7Dqc/tAUzdvy; yidun_tocken=9ca17ae2e6ffcda170e2e6eeccbc6f838e8dd4d1258fac8fb3c54e869e8faff761fb93f8bbd96aa78e9fbbe62af0feaec3b92a9cafe1aff86ffbbdf7bacc5f938f8eb2c14b8ee8ffd5dc40a887ab84e143b6b9eecda180e2e6eed5f27c81909ad0b349818ab7b5b640919c0091ec40a5e3f3c300; c_adb=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1553232625,1553252495,1553252603,1553253977; hasSub=true; dc_tos=pormiz; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1553254092
pragma: no-cache
referer: https://blog.csdn.net/weixin_41164823/article/details/80524100
user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
"""

# 去除参数头尾的空格并按换行符分割
headers = headers.strip().split('\n')

# 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}

# 使用json模块将字典转化成json格式打印出来
print(json.dumps(headers, indent=1))