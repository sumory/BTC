#coding:utf8

from mysql_database import addslashes, mysql_database
from pooled_mysql_database import pooled_mysql_database
import settings
	
def mysql_database_conf():
	host=settings.DB_HOST
	user=settings.DB_USER
	passwd=settings.DB_PWD
	db=settings.DB_DB
	port=settings.DB_PORT
	charset='utf8'
	# unix_socket=''
	return locals()
	
def database_pooling_conf():
	mincached=10
	maxcached=150
	maxconnections=150
	# maxshared=0
	# blocking=False
	# maxusage=None
	# setsession=None
	# reset=True
	# failures=None
	# ping=1
	return locals()
		

def get_mysql_db():
	return mysql_database(mysql_database_conf())
	
def get_pooled_mysql_db():
	return pooled_mysql_database(mysql_database_conf(), database_pooling_conf())
