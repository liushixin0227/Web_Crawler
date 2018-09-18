#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 0018 17:06
# @Author  : Liushixin
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import lxml
from selenium import webdriver
import aiohttp, aiodns
from bs4 import BeautifulSoup
import pyquery

# browser = webdriver.PhantomJS(executable_path=r'C:\SoftWare\Tools\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# browser.get('https://www.baidu.com')
# print(browser.current_url)

soup = BeautifulSoup('<p> Hello </p>', 'lxml')
print(soup.p.string)
