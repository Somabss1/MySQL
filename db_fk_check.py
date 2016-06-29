#!/usr/bin/python

import sys
from subprocess import call
import mysql.connector
from mysql.connector import errorcode
import mysql
from ConfigParser import SafeConfigParser
import string

parser=SafeConfigParser()
parser.read('config.ini')
config = {
   'user':parser.get('MySqlConnection', 'username'),
   'password':parser.get('MySqlConnection', 'password'), 
   'host':parser.get('MySqlConnection', 'host'),
   'database':parser.get('MySqlConnection', 'database'),
   'raise_on_warnings': True,
   'use_pure': False,
   'buffered':True,
	}

DB='database'
cnx = mysql.connector.connect(**config)
query = "SELECT `TABLE_NAME`, `COLUMN_NAME`, `REFERENCED_TABLE_NAME`, `REFERENCED_COLUMN_NAME`  FROM information_schema.KEY_COLUMN_USAGE WHERE TABLE_SCHEMA= %(database)s  AND REFERENCED_TABLE_SCHEMA IS NOT NULL;"
cursor = cnx.cursor()
cursor.execute(query, (config))
for row in cursor:
	TABLE_NAME=row[0]
	COLUMN_NAME=row[1]
	REFERENCED_TABLE_NAME=row[2]
	REFERENCED_COLUMN_NAME=row[3]	
	config1 = {
   	'TABLE_NAME':string.replace(row[0], "'", ""),
   	'COLUMN_NAME':string.replace(row[1], "'", ""),
   	'REFERENCED_TABLE_NAME':string.replace(row[2], "'", ""),
   	'REFERENCED_COLUMN_NAME':string.replace(row[3], "'", ""),
        }
	print "Checking %s.%s" % (TABLE_NAME,COLUMN_NAME)
	if(TABLE_NAME==REFERENCED_TABLE_NAME):
         	 #sql="SELECT t1.* FROM %(TABLE_NAME)s t1 LEFT JOIN %(REFERENCED_TABLE_NAME)s t2 ON (t1.%(COLUMN_NAME)s=t2.%(REFERENCED_COLUMN_NAME)s) WHERE t1.%(COLUMN_NAME)s IS NOT NULL AND t2.%(REFERENCED_COLUMN_NAME)s IS NULL"
		 sql="SELECT t1.* FROM " + TABLE_NAME + " t1 LEFT JOIN "+ REFERENCED_TABLE_NAME + " t2 ON (t1." +COLUMN_NAME +"=t2." + REFERENCED_COLUMN_NAME + ") WHERE t1."+COLUMN_NAME +" IS NOT NULL AND t2." + REFERENCED_COLUMN_NAME + " IS NULL"
      	else:
		#sql="SELECT %(TABLE_NAME)s.* FROM %(TABLE_NAME)s LEFT JOIN %(REFERENCED_TABLE_NAME)s ON (%(TABLE_NAME)s.%(COLUMN_NAME)s=%(REFERENCED_TABLE_NAME)s.%(REFERENCED_COLUMN_NAME)s) WHERE %(TABLE_NAME)s.%(COLUMN_NAME)s IS NOT NULL AND %(REFERENCED_TABLE_NAME)s.%(REFERENCED_COLUMN_NAME)s IS NULL"
		sql="SELECT "+ TABLE_NAME + ".* FROM "+ TABLE_NAME + " LEFT JOIN " + REFERENCED_TABLE_NAME + " ON (" + TABLE_NAME+"."+COLUMN_NAME+"="+REFERENCED_TABLE_NAME+"."+REFERENCED_COLUMN_NAME+") WHERE "+ TABLE_NAME+"."+COLUMN_NAME +" IS NOT NULL AND "+ REFERENCED_TABLE_NAME+"."+REFERENCED_COLUMN_NAME +" IS NULL"
	cursor1=cnx.cursor()
	cursor1.execute(sql, (config1))
	count = cursor1.rowcount
	if(count > 0):
	        print("Found {} Invalid Foreign Keys".format('count'))
		print sql
cnx.close()

