#!/usr/bin/python
#-*- coding: utf-8 -*-

#Generate useful info package of each email
#Author: SHEN HUIXIAN
#Date : 2015-09-09

import email
from get_header_info import get_header_info
from get_content_info import get_content_info


def generate_info_pkg_of_email( mail_path ):

    email_info_pkg = {}

    email_fp_1 = open( mail_path , "r" )
    email_fp_2 = open( mail_path , "r" )

    header_info = get_header_info( email_fp_1 )
    content_info = get_content_info( email_fp_2 )

    email_info_pkg["header"] = header_info
    email_info_pkg["content"] = content_info

    email_fp_1.close()
    email_fp_2.close()

    return email_info_pkg
