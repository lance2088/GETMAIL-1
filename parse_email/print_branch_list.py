#!/usr/bin/python
#-*- coding: utf-8 -*-

#Print the branch list
#Author: SHEN HUIXIAN
#Date : 2015-09-09


def print_branch_list( branch_list ):
    for i in range( 0 , len( branch_list ) ):
        for j in range( 0 , len( branch_list[i] ) ):
            email = branch_list[i][j]
            print email["header"]["subject"]          

        print '\n'
