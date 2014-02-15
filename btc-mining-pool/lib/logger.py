from __future__ import print_function

import datetime
import time
import settings


LOG_DIR = settings.LOG_DIR
scope_to_f = {}

def log(scope, *args):
    if(settings.LOG_ROLL):
        if(scope != 'block' and scope != 'submitblock' and scope != 'error'):
            suffix = time.strftime('%Y%m%d',time.localtime(time.time()))
            tmp = scope
            scope = tmp + '.' + suffix

            # close history log file from scope_to_f
            today = datetime.date.today()
            before = '%s' % (today-datetime.timedelta(days=2))
            to_close_file = tmp + '.' + before + '.log'
            if(to_close_file in scope_to_f):
                try:
                    print('close log %s' % to_close_file)
                    del scope_to_f[to_close_file]
                    scope_to_f[to_close_file].close()
                except Exception, e:
                    print('close log error %s' % e)



    
    if scope not in scope_to_f:
        log_file = '%s/%s.log' % (LOG_DIR, scope)
        scope_to_f[scope] = open(log_file, 'a+')
    print(str(datetime.datetime.now()), *args, file=scope_to_f[scope])
    scope_to_f[scope].flush()
