#!/usr/bin/python
#-*- coding: utf-8 -*-

#Check the folder /mail/new. If it's empty, then return 0 , else return 1 
#Author: SHEN HUIXIAN
#Date : 2015-09-09

import os
import sys
import os.path

home = os.environ['HOME']

def check_folder():

    folder_path= home + "/.getmail/mail/new"

    empty = False

    if( os.path.exists( folder_path ) == False ):
        print "No such path:" , folder_path
        sys.exit(0)

    else:
        for root,dirs, files in os.walk( folder_path ):
            if( len( files ) == 0 ):
                empty = True
    if( empty ):
        return 0
    else:
        return 1
