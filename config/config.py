#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-28 23:30
# @Author  : Liushixin
# @Site    : 
# @File    : config.py
# @Software: PyCharm
# encoding=utf8


class GlobalConfigration(object):
    '''
    '''
    ALARM_LEVEL_SERVER_CONDB_FAIL = 2
    REAL_OUTER_IP = '#IP_OUTER'
    if not REAL_OUTER_IP:
        REAL_OUTER_IP = '#IP_INNER'

    CURRENT_IP = '10.123.9.22'

    USE_PROXY_FLAG = 1
    if REAL_OUTER_IP.startswith('10.'):
        USE_PROXY_FLAG = 1

    DB_CONF = {
        'sdp': {
            'host': '10.55.142.100',
            'port': 4268,
            'user': 'd_outsite',
            'passwd': '71e5b04ae',
            'db': 'd_outsite_info',
            'charset': 'utf8',
        },

        'sdp.debug': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_outsite_info',
            'charset': 'utf8',
        },

        'crawler': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'search_id',
            'charset': 'utf8',
        },

        'crawler.release': {
            'host': '10.198.30.118',
            'port': 3527,
            'user': 'search_id',
            'passwd': '27bae32b3',
            'db': 'search_id',
            'charset': 'utf8',
        },

        'result_count': {  # 数据统计db，直接用正式环境吧
            # 'host' : '10.129.132.215',
            # 'port' : 3362,
            'zkname': 'm3362.d_crawler.cdb.com',  # 迁移使用zkname配置
            'user': 'd_crawler',
            'passwd': '188f99451',
            'db': 'd_crawler',
            'charset': 'utf8',
        },

        'test_ugc_video': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_ugc_video',
            'charset': 'utf8',
        },

        'ugc_video': {
            'host': '10.198.30.118',
            'port': 3870,
            'user': 'd_ugc_video',
            'passwd': 'e148303af',
            'db': 'd_ugc_video',
            'charset': 'utf8',
        },

        'relate_video': {
            'host': '10.240.64.138',
            'port': 3915,
            'user': 'd_ugc_info',
            'passwd': '5c37f4ce8',
            'db': 'd_related_ugc_info',
            'charset': 'utf8',
        },

        'sdp_task.release': {
            'host': '10.55.142.100',
            'port': 3389,
            'user': 'd_sdp_task',
            'passwd': '5742514c2',
            'db': 'd_sdp_task',
            'charset': 'utf8',
        },

        'sdp_task': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_sdp_task',
            'charset': 'utf8',
        },

        'complex_task': {
            'host': '10.198.30.118',
            'port': 4186,
            'user': 'complex_db',
            'passwd': '6851fd2bf',
            'db': 'd_complex_task',
            'charset': 'utf8',
        },

        'ugc_merge': {
            'host': '10.240.64.138',
            'port': 3427,
            'user': 'd_ugc_merge',
            'passwd': '2aec24047',
            'db': 'd_ugc_merge',
            'charset': 'utf8',
        },

        'ugc_merge.debug': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_ugc_merge',
            'charset': 'utf8',
        },

        'd_crawl_task': {
            'host': '100.65.203.225',
            'port': 3623,
            'user': 'd_crawl_task',
            'passwd': 'feb950453',
            'db': 'd_crawl_task',
            'charset': 'utf8',
        },

        'partition_task': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_crawl_partition_task',
            'charset': 'utf8',
        },
        'partition_task.release': {
            'host': '100.65.203.225',
            'port': 3623,
            'user': 'd_crawl_task',
            'passwd': 'feb950453',
            'db': 'd_crawl_partition_task',
            'charset': 'utf8',
        },
        'raw_user': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_raw_user',
            'charset': 'utf8',
        },
        'raw_user.release': {
            'host': '100.65.203.225',
            'port': 3407,
            'user': 'd_raw_video',
            'passwd': '53aab4fef',
            'db': 'd_raw_user',
            'charset': 'utf8',
        },
        'soft_video': {
            'host': '10.198.30.118',
            'port': 3870,
            'user': 'd_ugc_video',
            'passwd': 'e148303af',
            'db': 'd_site_long_ugc_temp',
            'charset': 'utf8',
        },
        'raw_album': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_raw_quality',
            'charset': 'utf8',
        },
        'raw_album.release': {
            'host': '100.65.203.225',
            'port': 3849,
            'user': 'd_raw_quality',
            'passwd': '904e849c9',
            'db': 'd_raw_quality',
            'charset': 'utf8',
        },
        'search_compare': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_album_monitor',
            'charset': 'utf8',
        },
        'search_compare.release': {
            'host': '100.65.203.225',
            'port': 3849,
            'user': 'd_raw_quality',
            'passwd': '904e849c9',
            'db': 'd_album_monitor',
            'charset': 'utf8',
        },
        'raw_album_final': {
            'host': '10.55.142.100',
            'port': 3905,
            'user': 'sdev',
            'passwd': 'sdev',
            'db': 'd_raw_quality_final',
            'charset': 'utf8',
        },
        'raw_album_final.release': {
            'host': '100.65.203.225',
            'port': 3624,
            'user': 'd_sdp_album',
            'passwd': 'ab102bbba',
            'db': 'd_raw_quality_final',
            'charset': 'utf8',
        },
    }

    MONGO_CONF = {
        'sdp': {
            'host': '10.238.3.234',
            'port': '27330',
            'user': 'sdp',
            'password': 'rs5x#a1t',
            'database': 'admin',
        },
        'sdp.debug': {
            'host': '10.123.9.22',
            'port': '27330',
            'user': 'sdp',
            'password': 'sdp',
            'database': 'admin',
        },
        'search_spider': {
            'host': '10.49.113.139',
            'port': '25018',
            'user': 'd_search_spider',
            'password': '17a69009a3',
            'database': 'd_search_spider',
            'zkname': 'm25018.d_search_spider.80000221.mongodb.com',
        },

    }

    REDIS_CONF = {
        'nameapi': 'sz0748.search_crawl_dispatch.redis.com',
        'key_ttl': 3600
    }

    list_config = list_crawler_settings.list_config

    DISPATCH_SERVER = {
        'host': '10.123.9.22',  # the remote host
        'port': 9000,  # the same port as used by the server
    }

    SDP_API_HTTP = {
        'host': '10.123.9.22',
        'port': 8080,
    }
    # SDP_API_HTTP = {
    #        'host' : 'api.sdp.com',
    #        'port' : 8080,
    #        }

    PROXY_NAME = {
        # 'host': 'proxy.v.qq.com',
        # 'host': 'proxy.videospider.qq.com',
        'host': '10.173.0.91',
        # 'host': '10.223.134.40',
        'host.douban': '10.248.108.37',
        'whitelist.dict': 'sdp.crawler.proxy.domain.whitelist.dict',
        'port': 8080,
    }

    QQLIVECFG_CONF = {
        'process_name': '../common/read_qqlivecfg',
        'config_id': 530,
    }

    MCALL_CONF = {
        'logic_crawler_frame': 210101827,  # 主调模块
        'logic_search_spider': 210102889,
        '/update_outer': {  # 精品区专辑视频入库
            'module': 210101831,
            'interface': 110304395,
        },
        '/ugc_video_import': {  # 入UGC_VIDEO库
            'module': 210101831,
            'interface': 110304397,
        },
        '/relate_video_import': {  # 相关视频入库
            'module': 210101831,
            'interface': 110304398,
        },
        '/update_long_ugc': {  # UGC视频更新
            'module': 210101831,
            'interface': 110304399,
        },
        'qiyi_crawl': {
            'module': 210101827,
            'interface': 110304723,
        },
        'qiyi_intention_crawl': {
            'module': 210101827,
            'interface': 110304723,
        },
        'qiyi_subtype_crawl': {
            'module': 210101827,
            'interface': 110304723,
        },
        'bilibili_crawl': {
            'module': 210101827,
            'interface': 110304724,
        },
        'youku_crawl': {
            'module': 210101827,
            'interface': 110304727,
        },
        'tudou_crawl': {
            'module': 210101827,
            'interface': 110304726,
        },
        'spider_mongodb': {
            'module': 210102890,
            'interface': 110308614,
        },
    }

    FRAME_SERVICE_HTTP = {
        'host': '10.209.7.38',
        # 'host' : '10.123.9.22',
        'port': '8081',
        'host.release': 'sdp.server.com',
        'host.slow': '10.209.7.38',
        'port.slow': '8082',
        'host.slow.release': 'slow.sdp.server.com',
    }

    FRAME_WRITE_SERVICE = {
        # 'action' : '/sdp_io/set',
        'action': '/sdp_io/set/{entity_type}',
        'iPassiveModuleId': 210102241,
        'iPassiveInterfaceId': 110305931,
        'youku.video_relation': {
            'module': 210101954,
            'interface': 110304860,
        },
        'qiyi.album_page': {
            'module': 210101954,
            'interface': 110306288,
        },
        'qiyi.video_relation': {
            'module': 210101954,
            'interface': 110305108,
        },
        '56.video_relation': {
            'module': 210101954,
            'interface': 110305089,
        },
        'bilibili.video_relation': {
            'module': 210101954,
            'interface': 110305191,
        },
    }

    TASK_SPAWN_SERVICE = {
        'action': '/spider/dispatch',
        'iPassiveModuleId': 210102098,
        'iPassiveInterfaceId': 110305337,
        'youku.video_relation': {
            'module': 210101969,
            'interface': 110304897,
        },
        'qiyi.album_page': {
            'module': 210101969,
            'interface': 110306287,
        },
        'qiyi.video_relation': {
            'module': 210101969,
            'interface': 110305109,
        },
        '56.video_relation': {
            'module': 210101969,
            'interface': 110305088,
        },
        'bilibili.video_relation': {
            'module': 210101969,
            'interface': 110305192,
        },
    }

    COROUTINE_NUM = 10

    FLASK_PORT = 16677


g_conf = GlobalConfigration()
