#coding:utf8

try:
	import MySQLdb as mysql
except Exception, e:
	print 'Warnning:', e
	mysql=None

from database_base import database_base

def addslashes(s):
	return mysql.escape_string(s)
		
class mysql_database(database_base):
	def __init__(self, conf):
		self.conf=conf
		self.conn=None
		
	def _mysql_conn_factory(self):
		conf=self.conf
		# print conf
		# raw_input()
		conn=None
		try:
			conn=mysql.connect(**conf)
			conn.autocommit(True)
		except Exception, e:
			print 'can not connect in mysql_database._mysql_conn_factory: %s' % e
		assert conn
		return conn
		
	def connect(self):
		if self.conn: return
		self.conn=self._mysql_conn_factory()
		
	def refresh(self):
		self.close()
		self.connect()
		
	def get_conn(self):
		if not self.conn:
			self.connect()
		else:
			try:
				self.conn.ping(True)	# attempt reconnection if lost
			except Exception, e:
				warn('ping failed in mysql_database.get_conn, now try refresh the connection: %s' % e)
				self.refresh()
				
		assert self.conn
		return self.conn
			
	def close(self):
		if not self.conn: return
		
		try:
			self.conn.commit()
			self.conn.close()
		except Exception, e:
			warn('failed closing connectiton in mysql_database.re_connect: %s' % e)
			# now force close
			del self.conn
		
		self.conn=None
	
	def get_cursor(self):
		return self.get_conn().cursor()
	
	def get_dict_cursor(self):
		return self.get_conn().cursor(mysql.cursors.DictCursor)
	
	def addslashes(self, s):
		return mysql.escape_string(s)
	
if __name__=='__main__':
	from edusns.filesystem.config import *
	db_conf=mysql_database_conf()
	pool_conf=database_pooling_conf()
	
	db1=mysql_database(db_conf)
	db=mysql_database(db_conf)
	for i in xrange(100):
		# if i%100==0: print i
		print db.conf
		print db.conn
		print db.addslashes('''a'b&p"m/ss''')
		print db.get_cursor()
		print db.conn
		
		print len(db.table('objects'))
		print len(db.table_dict('objects'))
		print db.one('select hash from objects')
		print db.first('select hash from objects')
		print db.one_dict('select stored_in_swift from objects')
		print len(db.all('select * from objects'))
		print len(db.all_dict('select * from objects'))
		
		
		print 'close db'
		db.close()
		print db.conn
		print db.get_conn()
		print db.get_conn()
		print db.get_dict_cursor()
		print db.conn
		print db.refresh()
		print db.conn
		
		print len(db.table('objects'))
		print len(db.table_dict('objects'))
		print db.one('select hash from objects')
		print db.first('select hash from objects')
		print db.one_dict('select stored_in_swift from objects')
		print len(db.all('select * from objects'))
		print len(db.all_dict('select * from objects'))
		
		
		
		
		
