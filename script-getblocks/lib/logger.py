from __future__ import print_function

import datetime

scope_to_f = {}

def log(scope, *args):
	if scope not in scope_to_f:
		scope_to_f[scope] = open('logs/%s.log' % scope, 'a')

	#print(str(datetime.datetime.now()), *args)
	print(str(datetime.datetime.now()), *args, file=scope_to_f[scope])
	scope_to_f[scope].flush()
