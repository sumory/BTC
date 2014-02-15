import time
import settings
import util
import logger
import gevent

class BlockUpdater(object):
    '''
        Polls upstream's getinfo() and detecting new block on the network.
        This will call registry.update_block when new prevhash appear.
        
        This is just failback alternative when something
        with ./bitcoind -blocknotify will go wrong. 
    '''
    
    def __init__(self, registry, bitcoin_rpc):
        self.bitcoin_rpc = bitcoin_rpc
        self.registry = registry
        self.clock = None
        gevent.spawn(self.schedule)
                        
    def schedule(self):
        while True:
            logger.log('track', 'schedule start')
            self.run()
            logger.log('track', 'schedule stop')
            gevent.sleep(settings.PREVHASH_REFRESH_INTERVAL)
                     
    def run(self):
        update = False
       
        try:
            if self.registry.last_block:
                current_prevhash = "%064x" % self.registry.last_block.hashPrevBlock
            else:
                current_prevhash = None
                
            prevhash = util.reverse_hash(self.bitcoin_rpc.prevhash())
            if prevhash and prevhash != current_prevhash:
                logger.log('debug', "New block! Prevhash: %s" % prevhash)
                update = True
            
            elif time.time() - self.registry.last_update >= settings.MERKLE_REFRESH_INTERVAL:
                logger.log('debug', "Merkle update! Prevhash: %s" % prevhash)
                update = True
            
            else:
                logger.log('debug', 'Nothing updated')

            if update:
                self.registry.update_block()

        except Exception, e:
            logger.log('error', "UpdateWatchdog.run failed %s" % e)

    
