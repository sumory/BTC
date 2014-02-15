import sys,os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(PROJECT_ROOT)


import settings
from lib import bitcoin_rpc

rpc = bitcoin_rpc.BitcoinRPC(settings.BITCOIN_RPC_HOST, settings.BITCOIN_RPC_PORT, settings.BITCOIN_RPC_USER, settings.BITCOIN_RPC_PASS)

block = rpc.getblock('00000000000000077e6eb274513df39076fc13ea85b775b8ed501b785b45f85d')
print block


