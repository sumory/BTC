'''
    Implements simple interface to bitcoind's RPC.
'''

import json
import base64
import geventhttpclient
import logger

class BitcoinRPC(object):
    
    def __init__(self, host, port, username, password):
        self.client = geventhttpclient.HTTPClient(host, port)
        self.credentials = base64.b64encode("%s:%s" % (username, password))
        self.headers = {
            'Content-Type': 'text/json',
            'Authorization': 'Basic %s' % self.credentials,
        }
        
    def _call_raw(self, data):
        logger.log('rpc', 'req:', data)
        res = self.client.post('/', body=data, headers=self.headers).read()
        logger.log('rpc', 'res:', res)
        return res
           
    def _call(self, method, params):
        return self._call_raw(json.dumps({
                'jsonrpc': '2.0',
                'method': method,
                'params': params,
                'id': '1',
            }))

    def submitblock(self, block_hex):
        resp = self._call('submitblock', [block_hex])
        if json.loads(resp)['result'] == None:
            return True
        else:
            return False

    def getblocktemplate(self):
        resp = self._call('getblocktemplate', [])
        return json.loads(resp)['result']

    def prevhash(self):
        resp = self._call('getwork', [])
        try:
            return json.loads(resp)['result']['data'][8:72]
        except Exception as e:
            logger.log('error', "Cannot decode prevhash %s" % str(e))
            raise
                                                  
    def validateaddress(self, address):
        resp = self._call('validateaddress', [address])
        return json.loads(resp)['result']

        
    def _pay_call_raw(self, data):
        logger.log('pay', 'req:', data)
        res = self.client.post('/', body=data, headers=self.headers).read()
        logger.log('pay', 'res:', res)
        return res

    def _pay_call(self, method, params):
        return self._pay_call_raw(json.dumps({
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': '1',
        }))

                                           
    def validateaddress2(self, address):
        resp = self._pay_call('validateaddress', [address])
        return json.loads(resp)['result']['isvalid']


    def settxfee(self, amount):
        resp = self._call('settxfee', [amount])
        return resp

    def walletpassphrase(self, passphrase, timeout):
        resp = self._call('walletpassphrase', [passphrase, timeout])
        return resp

    def sendtoaddress(self, address, amount):
        resp = self._call('sendtoaddress', [address, amount])
        return json.loads(resp)

    def getbalance(self, account):
        resp = self._pay_call('getbalance', [account])
        result = json.loads(resp)
        if(result['error']):
            logger.log('error','getbalance error %s' % result)
            return 0
        else:
            return result['result']

    def sendfrom(self, account, to_address, amount):
        resp = self._pay_call('sendfrom', [account, to_address, amount])
        result = json.loads(resp)
        if(result['error']):
            logger.log('error','sendfrom error %s' % result)
            return None
        else:
            return result['result']

    def getblock(self, blockhash):
        resp = self._call('getblock', [blockhash])
        return json.loads(resp)['result']

    def gettxout(self, txid, n):
        resp = self._call('gettxout', [txid, n])
        return json.loads(resp)['result']

