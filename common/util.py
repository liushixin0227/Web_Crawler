#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 22:22
# @Author  : Liushixin
# @Site    : 
# @File    : util.py
# @Software: PyCharm
from urllib.parse import urlsplit


def extract_domain_from_url(url):
    return urlsplit(url)[1] if url else 'None'
