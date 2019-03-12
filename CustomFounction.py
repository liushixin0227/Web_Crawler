#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 10:33 PM
# @Author  : Liushixin
# @Site    : 
# @File    : CustomFounction.py
# @Software: PyCharm

import requests
from lxml import etree

response = requests.get('https://all.wasu.cn/index/cid/11')
page = etree.HTML(response.content)

xpath_obj = page.xpath('//div[@class = "ws_all_span"]/ul/li[not(@class)]')

if not xpath_obj:
    print('解析失败！')

tag_dict = dict()

for tag_obj in xpath_obj:
    tag = tag_obj.xpath('./label/text()')[0]

    if tag.find('明星') == 0:
        continue
    else:
        print(tag.find('明星'))

    url_list = tag_obj.xpath('./a/@href')
    tag_dict[tag] = url_list

print(tag_dict)
