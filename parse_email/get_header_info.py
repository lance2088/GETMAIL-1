#!/usr/bin/python
#-*- coding: utf-8 -*-

#Get header info of each email
#Author: SHEN HUIXIAN
#Date : 2015-09-09

import email

def get_header_info( email_fp ):

        
    msg = email.message_from_file( email_fp )

    email_header_info = {}

    email_irt = msg.get("In-Reply-To")
    email_msg_id = msg.get("Message-ID")
    email_subject = msg.get("Subject")
    email_from = email.utils.parseaddr(msg.get("from"))[1]
    email_to = email.utils.parseaddr(msg.get("to"))[1]
    

    email_header_info["subject"] = email_subject
    email_header_info["from"] = email_from
    email_header_info["to"] = email_to
    email_header_info["msg_id"] = email_msg_id
    email_header_info["email_irt"] = email_irt

    return email_header_info
