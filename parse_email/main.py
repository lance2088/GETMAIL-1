#!/usr/bin/python
#-*- coding: utf-8 -*-

#Main 
#Author: SHEN HUIXIAN
#Date : 2015-09-09

from check_folder import check_folder
from return_emails_path import return_emails_path
from generate_info_pkg_of_email import generate_info_pkg_of_email
from check_content import check_content
from check_header import check_header
from parse import parse
from print_branch_list import print_branch_list

#Check if there is new emails or not.
result  = check_folder()

EMAIL_LIST = []
BRANCH_LIST = []
ID_SET = []
MAP = {}

if result is 1:
    emails = return_emails_path()
    count = 0


#For each email, we will check the content and the subject to determine whether it is a patch or not.
#Generate a EMAIL_LIST contains all the patches.
    for each_email in emails:
        email = generate_info_pkg_of_email( each_email )
        content_is_patch = check_content( email["content"] )

        if content_is_patch is 1 :
            header_is_patch = check_header( email["header"] )

            if header_is_patch is 1:
                if email["header"]["email_irt"] is None :
                    EMAIL_LIST.insert( 0 , email )
                else :
                    EMAIL_LIST.append( email )
                count = count + 1
                
else:
    print "No new file to deal with"


parse( EMAIL_LIST , BRANCH_LIST , MAP , ID_SET )

print_branch_list( BRANCH_LIST )
print count
