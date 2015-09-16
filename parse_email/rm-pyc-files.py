#!/usr/bin/python
#-*- coding : utf-8 -*-

import os
import os.path

file_path = []

for root , dirs , files in os.walk('.'):
	for name in files:
		if '.pyc' in name:
			file_path.append( root + '/' + name )

if len( file_path ) == 0:
	print 'NO FILE TO DELETE'
else:
	for i in range( 0 ,len( file_path) ):
		print file_path[i]+'\n'

	print '\nWant to delete?\n'
	print 'Yes : 1 , No : 2'

	flag = int( raw_input() )
	if flag == 1 :
		for i in range( 0 , len( file_path ) ):
			os.remove( file_path[i] )
	else:
		print "DO NOT DELETE!"
