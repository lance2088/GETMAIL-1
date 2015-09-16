#!/usr/bin/python
#-*- coding: utf-8 -*-

#Get the content info of email
#Author : SHEN HUIXIAN
#Date : 2015-09-09

import email

def get_content_info( email_fp ):

    msg = email.message_from_file( email_fp )
 
    for par in msg.walk():
        if not par.is_multipart():
            name = par.get_param( "name" )
            if name:
                pass
            else:
                content = par.get_payload( decode = True )
    return content
