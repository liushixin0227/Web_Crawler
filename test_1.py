#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 10:40 PM
# @Author  : Liushixin
# @Site    : 
# @File    : test_1.py
# @Software: PyCharm
import requests


class CustomFunction(object):
    def __init__(self):
        self.headers = ''

    def downloader(self, url):
        html = requests.get(url, headers=self.headers)
        return html
