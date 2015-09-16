#!/usr/bin/python
#-*- coding: utf-8 -*-

#Parse email
#Author: SHEN HUIXIAN
#Date : 2015-09-10


def parse( email_list , branch_list , email_map_branch  , id_set ): 

    for email in email_list :
        
        _set = []
        flag = False

        irt = email["header"]["email_irt"]
        msg_id = email["header"]["msg_id"]

        for i in range( 0 , len(id_set) ):
            if irt is None : 
                pass
            elif irt in id_set[i] : 
                flag = True
                index = i
                break
            if msg_id is None :
                pass
            elif msg_id in id_set[i] : 
                flag = True
                index = i
                break

        if flag is False :
            _set.append( irt )
            _set.append( msg_id )

            id_set.append( _set )

            email_queue = []
            email_queue.append( email )

            branch_list.append( email_queue )
            email_map_branch[msg_id] = branch_list.index( email_queue )

        else :
            key = id_set[index][1]
            _index = email_map_branch.get( key )
            branch_list[_index].append( email )
