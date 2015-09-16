#!/usr/bin/python
#-*- coding: utf-8 -*-

#Return path of all files
#Author: SHEN HUIXIAN
#Date : 2015-09-09

import os

home = os.environ['HOME']

def return_emails_path():
    file_list = home + '/.getmail/mail/new'

    files_path = []

    for file_name in os.listdir( file_list):

        file_path = home + "/.getmail/mail/new/" + file_name

        files_path.append( file_path )

    return files_path

