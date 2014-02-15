#!/bin/sh

today=`date +%Y%m%d`
python -c "import datetime; import time; print '%.2f GHash/s' % (9000 * 4 * 10 / (time.time() - time.mktime(datetime.datetime.strptime('`tail -9000 /data/asicme-pool/logs/hashrate.$today.log |head -1 |awk '{print $1" "$2}'`', '%Y-%m-%d %H:%M:%S.%f').timetuple())))"
