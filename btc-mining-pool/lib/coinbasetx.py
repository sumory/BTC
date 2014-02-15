import binascii
import halfnode
import struct
import util
import time

class CoinbaseTransaction(halfnode.CTransaction):
    '''Construct special transaction used for coinbase tx.
    It also implements quick serialization using pre-cached
    scriptSig template.'''
    
    extranonce_type = '>Q'
    extranonce_placeholder = struct.pack(extranonce_type, int('f000000ff111111f', 16))
    extranonce_size = struct.calcsize(extranonce_type)

    def __init__(self, coinbasers_value, total_value, flags, height, data):
        super(CoinbaseTransaction, self).__init__()
        
        #self.extranonce = 0
        
        if len(self.extranonce_placeholder) != self.extranonce_size:
            raise Exception("Extranonce placeholder don't match expected length!")

        tx_in = halfnode.CTxIn()
        tx_in.prevout.hash = 0L
        tx_in.prevout.n = 2**32-1
        tx_in._scriptSig_template = (
            util.ser_number(height) + binascii.unhexlify(flags) + util.ser_number(int(time.time())) + \
            chr(self.extranonce_size),
            # util.ser_string(coinbaser.get_coinbase_data() + data)
            util.ser_string(data)
        )
                
        tx_in.scriptSig = tx_in._scriptSig_template[0] + self.extranonce_placeholder + tx_in._scriptSig_template[1]
        self.vin.append(tx_in)
    
        total_value_share = sum([x[1] for x in coinbasers_value])
        used_value = 0

        for coinbaser, value in coinbasers_value:
            tx_out = halfnode.CTxOut()

            current_value = total_value * value / total_value_share

            tx_out.nValue = current_value
            used_value += current_value

            tx_out.scriptPubKey = coinbaser.get_script_pubkey()
            self.vout.append(tx_out)

        if used_value < total_value:
            self.vout[0].nValue += total_value - used_value

        # Two parts of serialized coinbase, just put part1 + extranonce + part2 to have final serialized tx
        self._serialized = super(CoinbaseTransaction, self).serialize().split(self.extranonce_placeholder)

    def set_extranonce(self, extranonce):
        # print repr(extranonce), self.extranonce_size
        if len(extranonce) != self.extranonce_size:
            raise Exception("Incorrect extranonce size")
        
        (part1, part2) = self.vin[0]._scriptSig_template
        self.vin[0].scriptSig = part1 + extranonce + part2
