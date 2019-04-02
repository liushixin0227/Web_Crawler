#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-28 23:28
# @Author  : Liushixin
# @Site    : 
# @File    : mongo.py
# @Software: PyCharm
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import datetime
from config import g_conf
from name_api import attemp_get_host_from_zk
import log


class MCallCode:
    NO_ERR = 0
    INSERT_MONGO_ERR = -1

class MongoClient:

    def __init__(self, key):
        self.key = key
        self.mongo_client = None

    def get_mongo_database(self):
        db_info = g_conf.MONGO_CONF.get(self.key, {})
        pool_size = int(g_conf.COROUTINE_NUM) / 2
        if not db_info or pool_size == 0:
            raise Exception(u'没有指定的MongoDB配置，name = %s' % self.key)
        ip, port = attemp_get_host_from_zk(db_info['zkname'])
        if not ip or not port:
            raise Exception(u'init ip or port fail，ip = {0}, port = {1}'.format(ip, port))
        connection = pymongo.MongoClient('mongodb://%s:%s@%s:%s/' % (db_info['user'], db_info['password'], ip, port), maxPoolSize = pool_size)
        if not connection:
            raise Exception(u'初始化mongoDB失败!')
        db = connection.get_database(db_info['database'])
        if not db:
            raise Exception(u'初始化mongoDB database失败!')
        return db

    def insert_mongo_one(self, crawl_page_dict):
        if not self.mongo_client:
            log.debug("mongo_client is null, init now")
            self.mongo_client = self.get_mongo_database()

        log.debug(self.mongo_client)

        date = datetime.date.today().strftime("%Y_%m_%d")
        mongo_table_name = 't_search_spider_' + date

        try:
            mongo_table = self.mongo_client.get_collection(mongo_table_name)
            if not mongo_table:
                log.error("failed to init mongo table. table_name = {0}".format(mongo_table_name))
                return False

        except Exception as e:
            log.error("failed to init mongo table. table_name = {0}".format(mongo_table_name))

        try:
            #将数据插入mongoDB
            object_id = mongo_table.insert_one(crawl_page_dict)
            if not object_id:
                log.error("failed to insert record into mongoDB. from mongodb.py")
            else:
                log.debug("success to insert data, from mongodb.py. ObjectId:{0}".format(object_id))
                return object_id
        except Exception as e:
            log.error("insert data into mongoDB throw Exception. url = {0}, exception = {1}".format(crawl_page_dict['url'], str(e)))




class MongoConnPool:
    pool = {}   #{name: conn}
    # mongoDB获取实例有两种模式
    # normal 普通模式，使用长连接，如果已经初始化连接，就复用原来的连接
    # force 强制初始化模式，该模式强制初始化mongoDBClient，为了解决长连接导致mongoDB负载不均衡，重新请求名字服务
    @staticmethod
    def get_instance(name, mode):
        if mode == "normal":
            if not MongoConnPool.pool.has_key(name):
                MongoConnPool.pool[name] = MongoClient(name)
        elif mode == "force":
            MongoConnPool.pool[name] = MongoClient(name)
        return MongoConnPool.pool[name]

