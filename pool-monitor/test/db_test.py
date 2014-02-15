import test_common
from database import *

try:
    db=get_pooled_mysql_db()
    print 'finished db initialization, got db connection'
except Exception, e:
    print 'failed db initialization: %s' % e
    exit()

def test():
    try:
        worker_name='sumory.w1'
        sql='select * from pool_withdraw'
        print(sql)
        one_dict=db.all_dict(sql)
        print one_dict
    except Exception, e:
        print 'db operation error: %s' % e
        exit()

test()



