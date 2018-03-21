#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 09:13:46 2018

@author: reillymaw
"""


def load_knapsack(things,knapsack_cap):
    """ You write your heuristic knapsack algorithm in this function using the argument values that are passed
             items: is a dictionary of the items no yet loaded into the knapsack
             knapsack_cap: the capacity of the knapsack (volume)
    
        Your algorithm must return two values as indicated in the return statement:
             my_team_number_or_name: if this is a team assignment then set this variable equal to an integer representing your team number;
                                     if this is an indivdual assignment then set this variable to a string with you name
            items_to_pack: this is a list containing keys (integers) of the items you want to include in the knapsack
                           The integers refer to keys in the items dictionary. 
   """
    lit = []
    for key, value in things.iteritems():
        temp = [key,value]
        lit.append(temp)
    sorte= sorted(lit, key=lambda tup: tup[1], reverse = True)

    my_team_number_or_name = "rmmaw"    # always return this variable as the first item
    items_to_pack = []    # use this list for the indices of the items you load into the knapsack
    load = 0.0            # use this variable to keep track of how much volume is already loaded into the backpack
    value = 0.0           # value in knapsack
    

    for i in range(len(sorte)-1):
        if load + sorte[i][1][0] <= knapsack_cap:
                items_to_pack.append(sorte[i][0])   
                value += sorte[i][1][1]
                load += sorte[i][1][0]
        else:
            i += 1
                 
    #print(items_to_pack)          
    #item_keys = [k for k in things.keys()]
    #pack_item = item_keys[0]
    #items_to_pack.append(pack_item)
    #load += things[pack_item][0]
    #value += things[pack_item][1]
    
    return my_team_number_or_name, items_to_pack   