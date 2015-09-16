#!/usr/bin/python
#-*- coding: utf-8 -*-

#Check the content to see whether it's a patch or not.
#Author: SHEN HUIXIAN
#Date : 2015-09-10

import re

def check_content( content ): 
    count = 0

    pattern_1 = re.compile(r"[0-9]* file[s]? changed[\W]? [0-9]* insertion[s]?[\s\S]*[\W]?" )
    result_1 = pattern_1.search( content )
    if result_1:
        count = 1

    pattern_2 = re.compile(r"[0-9]* file[s]? changed[\W]? [0-9]* deletion[s]?[\s\S]*[\W]? ")
    result_2 = pattern_2.search( content )
    if result_2:
        count = 1

    pattern_3 = re.compile(r"diff --git*?")
    result_3 = pattern_3.search( content )
    if result_3:
        count = 1

    if count is 1 :
        return 1
    else :
        return 0
