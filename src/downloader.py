#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 21:44
# @Author  : Liushixin
# @Site    : 
# @File    : downloader.py
# @Software: PyCharm
import datetime
import traceback

import requests

from common import log
from common.util import extract_domain_from_url


class Request(object):
    def __init__(self, method=None, url=None, headers=None, files=None, verify=False,
                 data=None, params=None, auth=None, cookies=None, hooks=None, json=None, timeout=None, proxies=None):
        super(Request, self).__init__()

        # Default empty dicts for dict params.
        data = [] if data is None else data
        files = [] if files is None else files
        headers = {} if headers is None else headers
        params = {} if params is None else params
        hooks = {} if hooks is None else hooks

        # self.hooks = default_hooks()
        # for (k, v) in list(hooks.items()):
        # self.register_hook(event=k, hook=v)

        self.method = method
        self.url = url
        self.headers = headers
        self.files = files
        self.verify = verify
        self.data = data
        self.json = json
        self.params = params
        self.auth = auth
        self.cookies = cookies

        self.timeout = timeout
        self.proxies = proxies


class Response(object):
    # __attrs__ = [
    # '_content', 'status_code', 'headers', 'url', 'history',
    # 'encoding', 'reason', 'cookies', 'elapsed', 'request'
    # ]
    def __init__(self, request, real_response):
        super(Response, self).__init__()
        self._request = request
        self.real_response = real_response

    @property
    def status_code(self):
        return self.real_response.status_code

    @property
    def headers(self):
        return self.real_response.headers

    @property
    def url(self):
        return self.real_response.url

    @property
    def encoding(self):
        return self.real_response.encoding

    @property
    def reason(self):
        return self.real_response.reason

    @property
    def request(self):
        return self._request

    @property
    def ok(self):
        return self.real_response.ok

    @property
    def content(self):
        return self.real_response.content

    @property
    def text(self):
        return self.real_response.text

    def json(self, **kwargs):
        return self.real_response.json(kwargs)

    def close(self):
        return self.real_response.close()


class Downloader(object):
    def __index__(self):
        pass

    def download(self, request):
        error_msg = ""
        real_response = None
        domain = extract_domain_from_url(request.url)
        log.debug("current proxies=[%s]" % request.proxies)
        if request.url:
            try:
                crawl_time = datetime.datetime.now()
                real_response = requests.request('get' if not request.method else request.method,
                                                 url=request.url,
                                                 data=request.data,
                                                 params=request.params,
                                                 headers=request.headers,
                                                 cookies=request.cookies,
                                                 proxies=request.proxies,
                                                 timeout=request.timeout,
                                                 verify=request.verify,
                                                 )
            except Exception as e:
                log.error("url=[%s]\n" % request.url + traceback.format_exc())
                error_msg = str(e)
            finally:
                # TODO:将下载数据存入日志数据库
                self.insert_log_table(data_obj=None)
                return Response(request, real_response)

    def insert_log_table(self, data_obj):
        pass
