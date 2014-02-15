#coding=utf-8

from __future__ import print_function

import datetime
import time
import zmq
import json
import os
from conf import config

LOG_DIR = config.ASYNC_LOG_DIR
LOG_ROLL = config.ASYNC_LOG_ROLL
LOG_PORT = config.ASYNC_LOG_SERVER_PORT
scope_to_f = {}



def pub_hashrate(connect_str):
    '''记录hashrate, sub端由java实现'''
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    pub.connect(connect_str)

    def log(*args):
        pub.send_string(' '.join(args))

    return log

def sub_logger():
    '''日志消费者'''
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)
    sub.bind('tcp://127.0.0.1:%i' % LOG_PORT)
    sub.setsockopt(zmq.SUBSCRIBE, "")
    last_minute = '0'
    print('sub_logger running....')
    while True:
        msg = sub.recv_json()
        minute = time.strftime('%M', time.localtime())
        if minute != last_minute:
            print('%s i am alive' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            last_minute = minute
        #print('%s %s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), json.dumps(msg)))
        log(msg['f'], *msg['c'])


def log_worker():
    '''日志发布者'''
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    pub.connect('tcp://127.0.0.1:%i' % LOG_PORT)


    def log(filename, *args):
        pub.send_json({'f':filename,'c':args})

    return log


def log(scope, *args):
    if LOG_ROLL is True:
        if scope != 'block' and scope != 'submitblock' and scope != 'error':
            suffix = time.strftime('%Y%m%d',time.localtime(time.time()))
            tmp = scope
            scope = tmp + '.' + suffix

            # close history log file from scope_to_f
            today = datetime.date.today()
            before = '%s' % (today-datetime.timedelta(days=2))
            to_close_file = tmp + '.' + before + '.log'
            if to_close_file in scope_to_f:
                try:
                    print('close log %s' % to_close_file)
                    del scope_to_f[to_close_file]
                    scope_to_f[to_close_file].close()
                except Exception, e:
                    print('close log error %s' % e)

    if scope not in scope_to_f:
        log_file = '%s/%s.log' % (LOG_DIR, scope)
        scope_to_f[scope] = open(log_file, 'a+')

    #print(len(scope_to_f))
    print(str(datetime.datetime.now()), *args, file=scope_to_f[scope])
    scope_to_f[scope].flush()
