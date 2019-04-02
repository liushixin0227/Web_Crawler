#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 21:44
# @Author  : Liushixin
# @Site    : 
# @File    : downloader.py
# @Software: PyCharm
import datetime
import traceback
import zlib

import bson
import requests
from retry import retry

from common import log
from common.util import extract_domain_from_url
from config import g_conf
from mongo import MongoConnPool, MCallCode


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


class CrawlPage(object):
    def __init__(self, trial_time=None, crawler_time=None, ttl=0, method=None, url=None, request_header=None, data=None,
                 json=None,
                 cookie=None, proxies=None, verify=None, status_code=None, encoding=None, response_headers=None,
                 response=None, error_msg=None):
        self.trial_time = trial_time
        self.crawler_time = crawler_time
        self.ttl = ttl
        self.method = method
        self.url = url
        self.request_header = request_header
        self.data = data
        self.json = json
        self.cookie = cookie
        self.proxies = proxies
        self.verify = verify
        self.status_code = status_code
        self.encoding = encoding
        self.response_headers = response_headers
        self.response = response
        self.error_msg = error_msg


class Downloader(object):
    def __index__(self):
        pass

    def init_mongo_mcall(self, iMainModuleIdKey, iPassiveModuleIdKey):
        iMainModuleId = g_conf.MCALL_CONF[iMainModuleIdKey]
        iPassiveModuleConf = self.get_mcall_conf(iPassiveModuleIdKey)
        if not iMainModuleId or not iPassiveModuleConf:
            log.error(
                "failed to init iMainModuleId or iPassiveModuleId!, iMainModuleId = {0}, iPassiveModuleConf = {1}".format(
                    iMainModuleId, iPassiveModuleConf))
            return False
        else:
            self.MCAPI = ModuleCallReportApi(iMainModuleId)
            self.MCAPI.iPassiveModuleId = iPassiveModuleConf['module']
            self.MCAPI.iModuleInterface = iPassiveModuleConf['interface']
            log.debug("success to init MCAPI.iMainModuleId = {0}, passive_module = {1}, passive_interface = {2}".format(
                iMainModuleId, self.MCAPI.iPassiveModuleId, self.MCAPI.iModuleInterface))
            return True

    def end_mcall(self, ret):
        self.MCAPI.iResult = ret
        self.MCAPI.iReturnValue = ret
        self.MCAPI.MCStop()

    @staticmethod
    def init_crawl_page(request, response, trial, error_msg, crawl_time):

        crawl_page = None
        try:
            # 处理请求发生错误的信息
            if error_msg != "" or not response:
                crawl_page = CrawlPage(trial_time=trial, crawler_time=crawl_time, ttl=10, method=request.method,
                                       url=request.url,
                                       request_header=request.headers, data=request.data, json=request.json,
                                       cookie=request.cookies,
                                       proxies=request.proxies, verify=request.verify, error_msg=error_msg)
                return crawl_page
        except Exception as e:
            log.error("init crawl page throw Exception. Exception = {0}".format(str(e)))
            return

        str_response = ""
        is_exception = False
        try:
            origin_coding = response.encoding
            if origin_coding:
                log.debug("origin_coding:{0}".format(origin_coding))
                str_response = response.text.decode(origin_coding).encode('utf-8')
            else:
                # 如果response返回的编码格式为空，强转utf-8编码
                str_response = response.text.encode('utf-8')

        except UnicodeDecodeError as unicode_error:
            log.error("init crawl page throw UnicodeDecodeError. UnicodeDecodeError = {0}".format(str(unicode_error)))
            str_response = "Unknown encoding format"

        except Exception as e:
            is_exception = True
            log.error("init crawl page throw Exception. Exception = {0}".format(str(e)))

        finally:
            if not is_exception:
                compress_response_content = zlib.compress(
                    str_response) if str_response and str_response != 'Unknown encoding format' \
                    else str_response
                crawl_page = CrawlPage(trial_time=trial, crawler_time=crawl_time, ttl=10, method=request.method,
                                       url=request.url, request_header=request.headers, data=request.data,
                                       json=request.json, cookie=request.cookies, proxies=request.proxies,
                                       verify=request.verify, status_code=response.status_code,
                                       encoding=response.encoding, response_headers=response.headers,
                                       response=bson.binary.Binary(compress_response_content))
                log.debug('init crawlpage with compress.')

        if not crawl_page:
            log.debug("failed to init crawl page")
            return
        return crawl_page

    def crawl_page_persistence(self, crawl_page):
        try:
            crawl_page_dict = crawl_page.__dict__
            if not crawl_page_dict:
                log.error("crawl_page_dict is null")
                return
            else:
                log.debug("success to transfer crawl page to dict, crawl page url = {0}".format(crawl_page_dict["url"]))
        except Exception as e:
            log.error("transfer crawl_page to dict throw exception. exception = {0}".format(str(e)))

        try:
            # 初始化mcall
            init_result = self.init_mongo_mcall("logic_search_spider", "spider_mongodb")
            if init_result:
                self.MCAPI.MCStart()
        except Exception as e:
            log.error("init mcall throw Exception. exception = {0}".format(str(e)))

        try:
            # 将数据插入mongoDB
            object_id = MongoConnPool.get_instance('search_spider', 'normal').insert_mongo_one(crawl_page_dict)
            if not object_id:
                log.error("failed to insert record into mongoDB. start to retry...")
                object_id_retry = MongoConnPool.get_instance('search_spider', 'force').insert_mongo_one(crawl_page_dict)
                if not object_id_retry:
                    log.error("failed to retry insert record into mongoDB. start to retry...")
                    if init_result:
                        self.end_mcall(MCallCode.INSERT_MONGO_ERR)
                else:
                    log.debug("success to retry insert data, ObjectId:{0}".format(object_id))
                    if init_result:
                        self.end_mcall(MCallCode.NO_ERR)
            else:
                log.debug("success to insert data, ObjectId:{0}".format(object_id))
                if init_result:
                    self.end_mcall(MCallCode.NO_ERR)

        except Exception as e:
            log.error(
                "insert data into mongoDB throw Exception. url = {0}, exception = {1}".format(crawl_page_dict['url'],
                                                                                              str(e)))

    @retry(tries=3)
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
                crawl_page = self.init_crawl_page(request, real_response, (total_trial - trial), error_msg,
                                                  crawl_time)

                # 将数据推送到mongoDB
                if not crawl_page:
                    log.error("failed to get crawl page")
                else:
                    self.crawl_page_persistence(crawl_page)

                return Response(request, real_response)

    def insert_log_table(self, data_obj):
        pass
