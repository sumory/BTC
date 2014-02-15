#coding=utf-8
import json
import gevent
import gevent.core
import gevent.server
from lib import bitcoin_rpc
from lib import logger
from lib import exceptions
import settings
import time
import random
from database import *


'''
   监控Block
   
   - 更新block的信息，如确认次数，该block挖到的币数等
'''

try:
    db = get_pooled_mysql_db()
    print 'succeed db initialization'
except Exception, e:
    print 'failed db initialization: %s' % e
    exit()


rpc = bitcoin_rpc.BitcoinRPC(settings.BITCOIN_RPC_HOST, settings.BITCOIN_RPC_PORT, settings.BITCOIN_RPC_USER, settings.BITCOIN_RPC_PASS)


def monitor_block():
    print '\n\n\n%s scan blocks..' % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    logger.log('scan_blocks', 'scan start')

    try:
        sql = 'select * from pool_block where confirmations < 120'
        #sql = 'select * from pool_block'
        all_blocks = db.all_dict(sql)
        logger.log('scan_blocks', 'need scan for %d blocks' % len(all_blocks))



        if(len(all_blocks) != 0):

            for b in all_blocks:
                try:
                    block_hash = b['hash']
                    block_id = int(b['id'])
                    
                    rpc_block = rpc.getblock(block_hash)
                    confirmations = int(rpc_block['confirmations'])
                    
                    db.run('update pool_block set confirmations=%d where id = %d' % (confirmations, block_id))
                except Exception, e:
                    logger.log('scan_blocks', 'exception %s' %e)
    except Exception, e:
        logger.log('scan_blocks','unknown excepiton %s' %e)
    finally:
        logger.log('scan_blocks','scan stop')


if __name__ == '__main__':
    forever = True
    if(forever is True):
        while True:
            monitor_block()
            gevent.sleep(5)
    else:
        monitor_block()
