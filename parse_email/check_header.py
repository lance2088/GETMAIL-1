#!/usr/bin/python
#-*- coding: utf-8 -*-

#Check the header to see whether it's a patch or not.
#Author: SHEN HUIXIAN
#Date : 2015-09-10

import re

def check_header( header ): 

    pattern = re.compile(r"RE*?" , re.I)
    result = pattern.match( header["subject"] )

    
    if result :
        return 0
    else:
        return 1
