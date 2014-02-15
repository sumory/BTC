#coding:utf8

try:
	import MySQLdb as mysql
	from DBUtils.PooledDB import TooManyConnections
	from DBUtils.PooledDB import PooledDB as pooled
except Exception, e:
	print 'Warnning:', e
	mysql=None
	TooManyConnections=None
	pooled=None

from mysql_database import mysql_database

class pooled_mysql_database(mysql_database):
	def __init__(this, mysql_conf, pool_conf):
		this.pool_conf=pool_conf
		mysql_database.__init__(this, mysql_conf)
		this.pool=pooled(this._mysql_conn_factory, **pool_conf)
		
	def get_conn(this):
		conn=None
		try_times=3
		for i in range(try_times+1):	# try to get a connection for 3 times
			try:
				conn=this.pool.connection()
				break
			except TooManyConnections:
				print '%s get_conn : failed to get connection for %d times: TooManyConnections' % (this, i)
				if i==try_times: raise
				sleep(1)	# now wait 1 second for the pool to be ready
		assert conn
		return conn
	
	def forbid_access_this_method(this):
		raise Exception('this method should not be called in pooled db')
	
	def close(this):
		this.forbid_access_this_method()
		
	def connect(this):
		this.forbid_access_this_method()
		
	def refresh(this):
		this.forbid_access_this_method()
		

if __name__=='__main__':
	pass
	
