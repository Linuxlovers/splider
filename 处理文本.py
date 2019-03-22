#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : BigC
# @Email   : big_it@126.com
# @File    : 处理文本.py
# @Software: PyCharm
import re

"""
处理采集工具的headers
将要处理的头信息放在head.txt中
结果将会输出在head.text.backup中
"""
file_name = 'head.text'
new_file = open(file_name + ".backup", 'w', encoding='utf-8')
with open(file_name, 'r', encoding='utf-8')as file:
    for line in file.readlines():
        # if re.search('\s', line):
        line_list = re.split(r'\s', line)
        print(re.search(r'\s',line))
        print(line_list)
        s = f"""\"{line_list[0]}":"{line_list[1]}\",\n"""
        new_file.write(s)
new_file.close()
