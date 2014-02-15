import util

import logger
import settings

# TODO: Add on_* hooks in the app
    
class SimpleCoinbaser(object):
    '''This very simple coinbaser uses constant bitcoin address
    for all generated blocks.'''
    
    def __init__(self, address, bitcoin_rpc):
        # Fire callback when coinbaser is ready
        
        self.address = address
        self.is_valid = False # We need to check if pool can use this address
        
        self.bitcoin_rpc = bitcoin_rpc
        self._validate()

    def _validate(self):
        d = self.bitcoin_rpc.validateaddress(self.address)
        self._address_check(d)
        
    def _address_check(self, result):
        if result['isvalid']:
            self.is_valid = True
            logger.log('debug', "Coinbase address '%s' is valid" % self.address)
            
        else:
            self.is_valid = False
            logger.log('debug', "Coinbase address '%s' is NOT valid!" % self.address)
        
    def _failure(self, failure):
        logger.log('error', "Cannot validate Bitcoin address '%s'" % self.address)
        raise
    
    def get_script_pubkey(self):
        if not self.is_valid:
            # Try again, maybe bitcoind was down?
            self._validate()
            raise Exception("Coinbase address %s is not validated!" % self.address)
        return util.script_to_address(self.address)    
                   
    def get_coinbase_data(self):
        return ''
