#coding:utf8

class database_base(object):
	def connect(self):
		'''connect to the host'''
		raise NotImplementedError
	
	def close(self):
		'''close the connection'''
		raise NotImplementedError

	def refresh(self):
		# self.close()
		# self.connect()
		'''refresh the connection'''
		raise NotImplementedError
		
	def get_conn(self):
		'''a proxy to get connection, useful for pooling connection 
		implementation the default behavior is to check the connection'''
		if not self.conn: self.connect()
		assert self.conn
		return self.conn
	
	def get_cursor(self):
		'''get nomal cursor, fields accessed by number, faster'''
		raise NotImplementedError
	
	def get_dict_cursor(self):
		'''get dict cursor, fields accessed by name, slower'''
		raise NotImplementedError
	
	def run(self, sql):
		cursor=self.get_cursor()
		cursor.execute(sql)
		ret=None
		if sql.strip()[:7].lower()=='insert ':
			try:
				insert_id=cursor.connection.insert_id()
				ret=insert_id
			except Exception, e:
				print 'got exception in run sql, %s, %s' % (type(e), e)
		else:
			rowcnt=cursor.rowcount
			ret=rowcnt
		cursor.close()
		return ret
		
	def insert(self, table, cols, vals):
		'''insert into table cols vals'''
		sql="insert into %s %s values %s" % (table, cols, vals)
		return self.run(sql)
		
	def update(self, table, set, where):
		'''update table set ... where ...'''
		sql="update %s set %s where %s" % (table, set, where)
		return self.run(sql)
	
	def delete(self, table, where):
		'''delete from table where ...'''
		sql="delete from %s where %s" % (table, where)
		return self.run(sql)
	
	def select(self, cols, table, where):
		'''select cols from table where ...'''
		sql="select %s from %s where %s" % (cols, table, where)
		return self.all(sql)
	
	def drop(self, table):
		'''drop table'''
		self.run("drop table "+table)
	
	def table(self, table):
		'''select * from table'''
		return self.all("select * from "+table)
	
	def table_dict(self, table):
		'''select * from table'''
		return self.all_dict("select * from "+table)
	
	def drop_db(self, dbname):
		return self.run("drop database "+dbname)
		
	def count(self, sql):
		'''return the count influenced by the opertion sql'''
		return self.run(sql)
	
	def first(self, sql):
		'''return the first col value of the first row'''
		cursor=self.get_cursor()
		cursor.execute(sql)
		row=cursor.fetchone()
		cursor.close()
		return row[0]
	
	def one(self, sql):
		'''return only one row from record set, accessed by id'''
		cursor=self.get_cursor()
		cursor.execute(sql)
		row=cursor.fetchone()
		cursor.close()
		return row
		
	def one_dict(self, sql):
		'''return only one row from record set, accessed by col name'''
		cursor=self.get_dict_cursor()
		cursor.execute(sql)
		row=cursor.fetchone()
		cursor.close()
		return row
		
	def all(self, sql):
		'''return all record, accessed by id'''
		cursor=self.get_cursor()
		cursor.execute(sql)
		rows=cursor.fetchall()
		cursor.close()
		return rows
	
	def all_dict(self, sql):
		'''return all record, accessed by col name'''
		cursor=self.get_dict_cursor()
		cursor.execute(sql)
		rows=cursor.fetchall()
		cursor.close()
		return rows
	
if __name__=='__main__':
	print database_base
	print database_base()
	print database_base().all_dict('')

