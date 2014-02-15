#coding=utf-8
import json
from lib import bitcoin_rpc
from lib import logger
import settings
import time
import random


rpc = bitcoin_rpc.BitcoinRPC(settings.BITCOIN_RPC_HOST, settings.BITCOIN_RPC_PORT, settings.BITCOIN_RPC_USER, settings.BITCOIN_RPC_PASS)

def getblocks():

    try:
        heights = range(263534,264609)[::-1]
        for i in heights:
            hash = rpc.getblockhash(i)
            block = rpc.getblock(hash)
            #print("%d %s %s" % (block['height'],time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(block['time'])),block['hash']))
            logger.log('block', '%d\t%s\t%s' % (block['height'],time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(block['time'])),block['hash']) )
    except Exception,e:
        print(e)
        logger.log('error','%s' % e)
    except:
        pass


if __name__ == '__main__':
    getblocks()
